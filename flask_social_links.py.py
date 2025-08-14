from flask import Flask
app = Flask(__name__)

@app.route('/')
def social():
    return '''
    <h2>Social Media Links</h2>
    <ul style="list-style-type: none; padding: 0;">
        <li style="display: inline-block; margin-right: 15px; text-align: center;">
            <a href="https://www.facebook.com" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" height="30" alt="Facebook"><br> Facebook
            </a>
        </li>
        <li style="display: inline-block; margin-right: 15px; text-align: center;">
            <a href="https://www.twitter.com" target="_blank">
                <img src="https://images.icon-icons.com/4029/PNG/512/twitter_x_new_logo_x_rounded_icon_256078.png" height="30" alt="Twitter"><br> Twitter
            </a>
        </li>
        <li style="display: inline-block; margin-right: 15px; text-align: center;">
            <a href="https://www.instagram.com" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/9/95/Instagram_logo_2022.svg" height="30" alt="Instagram"><br> Instagram
            </a>
        </li>
        <li style="display: inline-block; margin-right: 15px; text-align: center;">
            <a href="https://www.linkedin.com" target="_blank">
                <img src="https://media.licdn.com/dms/image/v2/D4D12AQFSkkazpND0Tg/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1696901179396?e=2147483647&v=beta&t=sg_aDp3g51FrQdFdKqc_c7Lz249Igbl5buOJvCcRzEY" height="30" alt="LinkedIn"><br> LinkedIn
            </a>
        </li>
        <li style="display: inline-block; margin-right: 15px; text-align: center;">
            <a href="https://www.github.com" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" height="30" alt="Github"><br> Github
            </a>
        </li>
        <li style="display: inline-block; margin-right: 15px; text-align: center;">
            <a href="https://www.youtube.com" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/4/42/YouTube_icon_%282013-2017%29.png" height="30" alt="YouTube"><br> YouTube
            </a>
        </li>
    </ul>
    <img src="https://media1.tenor.com/m/GfSX-u7VGM4AAAAd/coding.gif" height="150">
    '''

if __name__ == '__main__':
    app.run(debug=True, port=5006)
