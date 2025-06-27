from flask import Flask, render_template, request, jsonify, redirect, url_for
import requests
import os
from datetime import datetime
import openai
from dotenv import load_dotenv
import json
import time

# Charger les variables d'environnement
load_dotenv()

app = Flask(__name__)

class IPAnalyzer:
    def __init__(self):
        self.openai_client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.abuseipdb_key = os.getenv('ABUSEIPDB_API_KEY')
        self.shodan_key = os.getenv('SHODAN_API_KEY')
    
    def get_ipinfo_data(self, ip):
        """Récupère les informations de géolocalisation via ipinfo.io"""
        try:
            response = requests.get(f"https://ipinfo.io/{ip}/json", timeout=10)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(f"Erreur ipinfo.io: {e}")
        return None
    
    def get_ip_api_data(self, ip):
        """Récupère les informations détaillées via ip-api.com"""
        try:
            response = requests.get(f"http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,asname,mobile,proxy,hosting,query", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success':
                    return data
        except Exception as e:
            print(f"Erreur ip-api.com: {e}")
        return None
    
    def get_abuseipdb_data(self, ip):
        """Vérifie la réputation via AbuseIPDB"""
        if not self.abuseipdb_key:
            return None
        
        try:
            headers = {
                'Key': self.abuseipdb_key,
                'Accept': 'application/json'
            }
            params = {
                'ipAddress': ip,
                'maxAgeInDays': 90,
                'verbose': ''
            }
            response = requests.get('https://api.abuseipdb.com/api/v2/check', 
                                  headers=headers, params=params, timeout=10)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(f"Erreur AbuseIPDB: {e}")
        return None
    
    def get_shodan_data(self, ip):
        """Récupère les informations de ports ouverts via Shodan"""
        if not self.shodan_key:
            return None
        
        try:
            response = requests.get(f"https://api.shodan.io/shodan/host/{ip}?key={self.shodan_key}", timeout=10)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(f"Erreur Shodan: {e}")
        return None
    
    def generate_ai_report(self, ip_data):
        """Génère un rapport compréhensible avec OpenAI"""
        if not os.getenv('OPENAI_API_KEY'):
            return "Rapport IA non disponible - clé API manquante"
        
        try:
            # Préparer les données pour l'IA
            summary = f"""
            Analyse de l'adresse IP: {ip_data.get('ip', 'N/A')}
            
            Géolocalisation:
            - Pays: {ip_data.get('country', 'N/A')}
            - Ville: {ip_data.get('city', 'N/A')}
            - ISP: {ip_data.get('isp', 'N/A')}
            - Organisation: {ip_data.get('org', 'N/A')}
            
            Sécurité:
            - Score d'abus: {ip_data.get('abuse_confidence', 0)}%
            - Signalements: {ip_data.get('usage_type', 'N/A')}
            - Proxy/VPN: {ip_data.get('is_proxy', False)}
            - Hébergement: {ip_data.get('is_hosting', False)}
            
            Ports ouverts: {len(ip_data.get('ports', []))} ports détectés
            """
            
            response = self.openai_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Tu es un expert en cybersécurité. Analyse ces données d'IP et fournis un rapport de sécurité clair et compréhensible en français, en évaluant les risques potentiels."},
                    {"role": "user", "content": summary}
                ],
                max_tokens=500,
                temperature=0.3
            )
            
            return response.choices[0].message.content
        except Exception as e:
            print(f"Erreur OpenAI: {e}")
            return f"Erreur lors de la génération du rapport IA: {str(e)}"
    
    def analyze_ip(self, ip):
        """Analyse complète d'une adresse IP"""
        result = {
            'ip': ip,
            'timestamp': datetime.now().isoformat(),
            'data': {},
            'ai_report': '',
            'map_link': ''
        }
        
        # Collecte des données
        print(f"Analyse de {ip}...")
        
        # ipinfo.io
        ipinfo_data = self.get_ipinfo_data(ip)
        if ipinfo_data:
            result['data']['ipinfo'] = ipinfo_data
        
        # ip-api.com
        ipapi_data = self.get_ip_api_data(ip)
        if ipapi_data:
            result['data']['ipapi'] = ipapi_data
        
        # AbuseIPDB
        abuse_data = self.get_abuseipdb_data(ip)
        if abuse_data:
            result['data']['abuseipdb'] = abuse_data
        
        # Shodan
        shodan_data = self.get_shodan_data(ip)
        if shodan_data:
            result['data']['shodan'] = shodan_data
        
        # Consolidation des données pour l'IA
        consolidated = self.consolidate_data(result['data'])
        result['consolidated'] = consolidated
        
        # Génération du rapport IA
        result['ai_report'] = self.generate_ai_report(consolidated)
        
        # Lien Google Maps
        lat = consolidated.get('lat')
        lon = consolidated.get('lon')
        if lat and lon:
            result['map_link'] = f"https://www.google.com/maps?q={lat},{lon}"
        
        return result
    
    def consolidate_data(self, data):
        """Consolide les données de toutes les sources"""
        consolidated = {}
        
        # Données de base
        if 'ipapi' in data:
            api_data = data['ipapi']
            consolidated.update({
                'country': api_data.get('country'),
                'city': api_data.get('city'),
                'region': api_data.get('regionName'),
                'lat': api_data.get('lat'),
                'lon': api_data.get('lon'),
                'isp': api_data.get('isp'),
                'org': api_data.get('org'),
                'is_proxy': api_data.get('proxy', False),
                'is_hosting': api_data.get('hosting', False),
                'timezone': api_data.get('timezone')
            })
        
        # Données ipinfo en complément
        if 'ipinfo' in data:
            ipinfo_data = data['ipinfo']
            if not consolidated.get('country'):
                consolidated['country'] = ipinfo_data.get('country')
            if not consolidated.get('city'):
                consolidated['city'] = ipinfo_data.get('city')
        
        # Données de sécurité AbuseIPDB
        if 'abuseipdb' in data and 'data' in data['abuseipdb']:
            abuse_info = data['abuseipdb']['data']
            consolidated.update({
                'abuse_confidence': abuse_info.get('abuseConfidencePercentage', 0),
                'is_whitelisted': abuse_info.get('isWhitelisted', False),
                'usage_type': abuse_info.get('usageType', 'Unknown'),
                'total_reports': abuse_info.get('totalReports', 0)
            })
        
        # Données Shodan
        if 'shodan' in data:
            shodan_info = data['shodan']
            consolidated.update({
                'ports': shodan_info.get('ports', []),
                'hostnames': shodan_info.get('hostnames', []),
                'vulns': list(shodan_info.get('vulns', {}).keys()) if 'vulns' in shodan_info else []
            })
        
        return consolidated

analyzer = IPAnalyzer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    ip = request.form.get('ip')
    if not ip:
        return jsonify({'error': 'Adresse IP requise'}), 400
    
    try:
        result = analyzer.analyze_ip(ip)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/report/<ip>')
def report(ip):
    try:
        result = analyzer.analyze_ip(ip)
        return render_template('report.html', data=result)
    except Exception as e:
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)