from flask import Flask, redirect, request, jsonify

app = Flask(__name__)

@app.route('/get-video/mxfliofc-vip/URL', methods=['GET'])
def redirect_video():
    try:
        # Obter a URL completa da solicitação
        original_url = request.args.get('url')
        
        if not original_url:
            return jsonify({'error': 'URL não fornecida'}), 400
        
        # Extrair o ID do vídeo da URL fornecida
        video_id = original_url.split('/')[-1]
        
        # Construir a nova URL modificada
        base_url = original_url.rsplit('/', 2)[0]
        new_url = f"{base_url}/f/{video_id}_x"
        
        # Redirecionar para a nova URL
        return redirect(new_url, code=302)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
  
