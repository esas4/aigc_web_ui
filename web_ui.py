import gradio as gr

css = """
.gradio-container {background-color: #0B1013}
#chatbot_com {color: blue}
footer {visibility: hidden}
"""

js = """
function createGradioAnimation() {
    var container = document.createElement('div');
    container.id = 'gradio-animation';
    container.style.fontSize = '2em';
    container.style.fontWeight = 'bold';
    container.style.textAlign = 'center';
    container.style.marginBottom = '20px';
    container.style.color = "white";
    container.style.fontFamily = 'Microsoft Yahei UI';

    var text = "欢迎来到孟及科技!";
    for (var i = 0; i < text.length; i++) {
        (function(i){
            setTimeout(function(){
                var letter = document.createElement('span');
                letter.style.opacity = '0';
                letter.style.transition = 'opacity 0.5s';
                letter.innerText = text[i];

                container.appendChild(letter);

                setTimeout(function() {
                    letter.style.opacity = '1';
                }, 50);
            }, i * 250);
        })(i);
    }

    var gradioContainer = document.querySelector('.gradio-container');
    gradioContainer.insertBefore(container, gradioContainer.firstChild);

    return 'Animation created';
}
"""

chat_history = [("数字人是什么？", "数字人是运用数字技术创造出来的与人类形象接近的数字化人物形象。")]
avatar_human_video = "/home/ecs-user/web_data/avatar3d/ngp_ep0019_audio.mp4" # replace with your own video path
avatar_cartoon_video = '/avatar/Demo_264.mp4' # replace with your own video path


def greet(input, chatbot_human):
    pass

def greet2d(input, chatbot_human):
    pass


with gr.Blocks(title="孟及科技（上海）有限公司", js=js, css=css, theme=gr.themes.Monochrome(radius_size=gr.themes.sizes.radius_md)) as avatar1:
    with gr.Row():
        avatar_human=gr.Video(label="视频", scale=0.5, interactive=False, value=avatar_human_video, height=500, autoplay=True)
        with gr.Column():
            chatbot_human=gr.Chatbot(label="对话记录", value=chat_history, height=400)   
            msg_human=gr.Textbox(label="你的问题", value="你好")
    
    msg_human.submit(greet, [msg_human, chatbot_human], [chatbot_human, avatar_human])  


with gr.Blocks(title="孟及科技（上海）有限公司", js=js, css=css, theme=gr.themes.Monochrome(radius_size=gr.themes.sizes.radius_md)) as avatar2:
    with gr.Row():
        avatar_cartoon=gr.Video(label="视频", scale=0.5, interactive=False, value=avatar_cartoon_video, height=500, autoplay=True)
        with gr.Column():
            chatbot_cartoon=gr.Chatbot(label="对话记录", value=chat_history, height=400)   
            msg_cartoon=gr.Textbox(label="你的问题", value="你好")
    
    msg_cartoon.submit(greet2d, [msg_cartoon, chatbot_cartoon], [chatbot_cartoon, avatar_cartoon])  


with gr.Blocks(title="孟及科技（上海）有限公司", js=js, css=css, theme=gr.themes.Soft()) as demo4:

    # 在gradio生成的界面添加返回主页的链接
    # gr.Markdown("""
    #     <div style="display: flex; justify-content: center;flex-wrap:wrap">
    #         <div style="width: 50%;display: flex; flex-direction: column; justify-content: center; align-items: center;min-width:20rem">
    #             <div style="text-align: left;">
    #                 <h2 style="color:white; font-family:sans-serif;">虚拟数字人</h2>
    #                 <h3 style="color:white; font-family:sans-serif;">- 强大自研能力，打造行业领先的多模态交互技术</h3>
    #                 <h3 style="color:white; font-family:sans-serif;">- 智能播报、直播、交互型等多种数字人产品方案</h3>
    #                 <h3 style="color:white; font-family:sans-serif;">- 为企业提供一站式、拟人化的客户服务</h3>
    #                 <h2>
    #                     <a href="https://baidu.com" style="color: white; background-color: grey; padding: 10px; transition: background-color 0.3s ease; border: 2px solid transparent; margin-left: 5px; margin-right: 10px; text-decoration: none; border-radius: 5px;">购买咨询</a>
    #                     <a href="https://bing.com" style="color: black; background-color: white; padding: 10px; transition: background-color 0.3s ease; border: 2px solid transparent; text-decoration: none; border-radius: 5px; margin-left: 80px;">关于我们</a>
    #                 </h2>
    #             </div>
    #         </div>
    #         <div style="width: 50%; display: flex; justify-content: center; align-items: center; margin-top: 2vw;min-width:288px">
    #             <video width="500" height="400" controls>
    #             <source src="https://portal.volccdn.com/obj/volcfe/avatar/can.mp4" type="video/mp4">
    #             </video>
    #         </div>
    #     </div>
    #         """)
    intro_html="""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        * {
            padding: 0;
            margin: 0;
        }
        .video_class{
            width: 50%; 
            display: flex; 
            justify-content: center; 
            align-items: center; 
            margin-top: 2vw;
            min-width:288px;
        }
        .video_display{
            width:500px;
            height:400px;
        }
        @media (max-width:768px){
            .video_display{
                width: 95%;
            }
        }
    </style>
    </head>
    <body>
        <div style="display: flex; justify-content: center;flex-wrap:wrap">
            <div style="width: 50%;display: flex; flex-direction: column; justify-content: center; align-items: center;min-width:20rem">
                <div style="text-align: left;">
                    <h2 style="color:white; font-family:sans-serif;">虚拟数字人</h2>
                    <h3 style="color:white; font-family:sans-serif;">- 强大自研能力，打造行业领先的多模态交互技术</h3>
                    <h3 style="color:white; font-family:sans-serif;">- 智能播报、直播、交互型等多种数字人产品方案</h3>
                    <h3 style="color:white; font-family:sans-serif;">- 为企业提供一站式、拟人化的客户服务</h3>
                    <h2 style="margin-top: 20px; margin-bottom: 20px; display: flex; justify-content: space-between; align-items: center;">
                        <a href="https://baidu.com" style="color: white; background-color: grey; padding: 5px; transition: background-color 0.3s ease; border: 2px solid transparent; margin-left: 10px; text-decoration: none; border-radius: 5px;">购买咨询</a>
                        <a href="https://bing.com" style="color: black; background-color: white; padding: 5px; transition: background-color 0.3s ease; border: 2px solid transparent; text-decoration: none; border-radius: 5px; margin-right:10px;">关于我们</a>
                    </h2>
                </div>
            </div>
            <div class="video_class">
                <video class="video_display" controls>
                <source src="https://portal.volccdn.com/obj/volcfe/avatar/can.mp4" type="video/mp4">
                </video>
            </div>
        </div>
    </body>
    </html>
    """
    gr.HTML(intro_html)

    gr.Markdown("""
        <div style="display: flex; justify-content: center;">
            <h2> 
                <span style="color:white">用户体验区</span>
            </h2>
        </div>
                """)
    gr.TabbedInterface([avatar1, avatar2], ["3D数字分身", "动画数字人"])

    display_html="""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        * {
            padding: 0;
            margin: 0;
        }
        .pics {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 20vh;
            flex-direction: column;
        }
        .shell{
            flex-wrap:wrap;
            width: 95%;
            height: 300px;
            display: flex;
            margin: 0 auto;
            margin-top: 10px
        }
        .box{
            flex: 1;
            overflow: hidden;
            transition: .5s;
            margin: 0 20px;
            box-shadow: 10px 10px 20px rgba(0, 0, 0, .5);
            border-radius: 20px;
            border: 10px solid #000;
            background-color: lightgray;
            max-height:300px;
        }
        .box>img{
            width: 200%;
            height: 85%;
            object-fit: cover;
            transition: .5s;
        }
        .box>span{
            font-family:sans-serif;
            text-align: center;
            height: 15%;
            display: flex;
            justify-content: center;
            align-items: center;
            font-weight: bold;
            font-size: 17px;
        }
        .box:hover{
            flex-basis: 40%;
        }
        .box:hover>img{
            width: 100%;
            height: 100%;
            object-fit:contain;
            max-height:300px;
        }
        @media (max-width:768px){
            .shell {
                flex-wrap: nowrap;
                overflow-x: auto; 
            }
            .box {
                flex: 0 0 auto; 
                width: 70%;
                margin: 0 5px; 
            }
            .box:hover {
                flex-basis: auto;
                width: 80%; 
            }
            .box:hover>img{
                width: 100%;
                height: 100%;
                object-fit:contain;
                max-height:300px;
            }
        }
    </style>
    </head>
    <body>
        <div style="display: flex; justify-content: center;">
            <h2> 
                <span style="color:white">功能展示</span>
            </h2>
        </div>
        <pics>
        <div class="shell">
            <div class="box">
                <img src="https://img2.baidu.com/it/u=4157674616,4124693857&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=1082" alt="chatbot">
                <span>剧本创作</span>
            </div>
            <div class="box">
                <img src="https://img0.baidu.com/it/u=3738152761,2996096054&fm=253&fmt=auto&app=138&f=PNG?w=500&h=889" alt="summary">
                <span>语音合成</span>
            </div>
            <div class="box">
                <img src="https://img0.baidu.com/it/u=778706271,2790085059&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500" alt="Text2Video">
                <span>本地知识库问答</span>
            </div>
            <div class="box">
                <img src="https://img0.baidu.com/it/u=2208339082,1662901984&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500" alt="Text2Voice">
                <span>动画数字人制作</span>
            </div>
            <div class="box">
                <img src="https://img2.baidu.com/it/u=948556055,246785504&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=888" alt="Text2Voice">
                <span>3D数字分身</span>
            </div>
            <div class="box">
                <img src="https://img1.baidu.com/it/u=3859042543,1974522143&fm=253&fmt=auto&app=138&f=JPEG?w=333&h=500" alt="Text2Voice">
                <span>动画制作</span>
            </div>
            <div class="box">
                <img src="https://img1.baidu.com/it/u=3859042543,1974522143&fm=253&fmt=auto&app=138&f=JPEG?w=333&h=500" alt="Text2Voice">
                <span>一键换衣</span>
            </div>
            <div class="box">
                <img src="https://img1.baidu.com/it/u=3859042543,1974522143&fm=253&fmt=auto&app=138&f=JPEG?w=333&h=500" alt="Text2Voice">
                <span>视频编辑</span>
            </div>
        </div>
        </pics>
    </body>
    </html>
    """
    gr.HTML(display_html)
    #,title="孟及科技(上海)有限公司"
    footer_html = """
    <!DOCTYPE html>
    <html>

    <head>
    <style>
    .footer {
        background-color: lightgray;
        padding: 10px;
        text-align: center;
        }

    .footer a {
        margin-right: 10px;
        text-decoration: none;
        color: black;
        }
    </style>
    </head>

    <body>
    <div class="footer">
        <div>
        <a href="#">关于</a>
        <a href="#">联系我们</a>
        <a href="#">使用条款</a>
        <a href="#">隐私</a>
        </div>
        <div>© 孟及科技（上海）有限公司 2024. All Rights Reserved.</div>
    </div>
    </body>

    </html>
    """
    gr.HTML(footer_html)
    
    
demo4.launch(share=True)