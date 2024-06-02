import gradio as gr

css = """
.gradio-container {background-color: #0B1013}
#chatbot_com {color: blue}
footer {visibility: hidden}
#component-19-button {font-size: 18px}
#component-20-button {font-size: 18px}
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
            <div class="video_class" style="margin-top:20px">
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

    gr.Markdown("""
            <div style="display: flex; justify-content: center;">
                <h2> 
                    <span style="color:white">功能展示</span>
                </h2>
            </div>
                """)

    display_html="""
<!DOCTYPE html>
<html lang="en" >
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <head>
        <style>
            * {
                margin: 0;
                padding: 0;
                border: 0;
                font-size: 100%;
                font: inherit;
                vertical-align: baseline;
            }
      .banner-container {
        width: 90%;
        height:300px;
        overflow: hidden;
        position: relative;
        margin: 0 auto;
      }
      .banner-img-container {
        display: flex;
        align-self: flex-start;
        height: 80%;
        width: 800%;
        transition: transform 0.5s ease;
      }
      .banner-item {
        height: 100%;
        display: flex;
        min-width: 12.5%;
        max-width: 12.5%;
      }
      .item-img {
        height: 100%;
        width: 60%;
        display: flex;
        align-items: center;
        justify-content: center;
      }
      .item-img img {
        object-fit: contain;
        height: 100%;
        width: 100%;
      }
      .banner-text {
        width: 40%;
      }
      .btn {
        width: 1rem;
        height: 1rem;
        border-radius: 0.5rem;
        border: 2px solid black;
        box-sizing: border-box;
        cursor: pointer;
      }
      .btn:active {
        background-color: rgb(108, 179, 246);
      }
      .banner-tool {
        margin-top: 20px;
        width: 20rem;
        display: flex;
        justify-content: space-around;
      }
      /* 设置轮播图动画 */
      #banner-control-1:checked ~ .banner-img-container {
        transform: translateX(0%);
      }
      #banner-control-2:checked ~ .banner-img-container {
        transform: translateX(-12.5%);
      }
      #banner-control-3:checked ~ .banner-img-container {
        transform: translateX(-25%);
      }
      #banner-control-4:checked ~ .banner-img-container {
        transform: translateX(-37.5%);
      }
      #banner-control-5:checked ~ .banner-img-container {
        transform: translateX(-50%);
      }
      #banner-control-6:checked ~ .banner-img-container {
        transform: translateX(-62.5%);
      }
      #banner-control-7:checked ~ .banner-img-container {
        transform: translateX(-75%);
      }
      #banner-control-8:checked ~ .banner-img-container {
        transform: translateX(-87.5%);
      }
      input[name="radio-set"] {
        position: absolute;
        bottom:0;
        z-index: 9;
        border: 1px solid white;
        background-color:white;
        border-radius:1rem;
        box-sizing: border-box;
      }
      input[name="radio-set"]:checked {
        background-color:#2483eb;
      }
      #banner-control-1 {
        left: calc(50% - 7rem);
      }
      #banner-control-2 {
        left: calc(50% - 5rem);
      }
      #banner-control-3 {
        left: calc(50% - 3rem);
      }
      #banner-control-4 {
        left: calc(50% - 1rem);
      }
      #banner-control-5 {
        left: calc(50% + 1rem);
      }
      #banner-control-6 {
        left: calc(50% + 3rem);
      }
      #banner-control-7 {
        left: calc(50% + 5rem);
      }
      #banner-control-8 {
        left: calc(50% + 7rem);
      } 
    
    .banner-container .prev, .banner-container .next{
        width: 40px;
        height: 70px;
        /* border: 2px solid black; */
        position: absolute;
        top: 50%;
        margin-top: -70px;
        z-index: 9;
        background-size: 100% 100%;
        background-repeat: no-repeat;
    }

    .banner-container .prev{
        left: 0px;
        background-image: url(images/g_left.png);
    }

    .banner-container .next{
        right: 0px;
        background-image: url(images/g_right.png);
    }

    .banner-container .prev:hover{
        background-image: url(images/b_left.png);
        z-index: 9;
        background-size: 100% 100%;
        background-repeat: no-repeat;
    }

    .banner-container .next:hover{
        background-image: url(images/b_right.png);
        z-index: 9;
        background-size: 100% 100%;
        background-repeat: no-repeat;
    }

       .banner-item .banner-text {
                width: 40%;
                background-color: white;
                box-sizing: border-box;
                margin: 10px;
                padding: 10px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                line-height: 1.5;
                height:90%;
                overflow: auto;
            }

            .banner-item .banner-text h3 {
                margin-bottom: 10px; /* 添加一些间距 */
                font-size: 20px;
                font-weight: bold;
            }

            .banner-item .banner-text li {
                margin-bottom: 5px; /* 添加一些间距 */
                font-size: 16px;
            }

        </style>
        <script>
            document.addEventListener("DOMContentLoaded", function() {
              const prevButton = document.querySelector('.prev');
              const nextButton = document.querySelector('.next');
              const radioButtons = document.querySelectorAll('input[name="radio-set"]');
          
              let currentIndex = 0; // 起始索引设置为0，对应第一张图片
          
              // 点击“上一张”按钮
              prevButton.addEventListener('click', function() {
                if (currentIndex === 0) {
                  currentIndex = radioButtons.length - 1; // 如果是第一张图，跳到最后一张图
                } else {
                  currentIndex--; // 否则索引减1
                }
                radioButtons[currentIndex].checked = true;
              });
          
              // 点击“下一张”按钮
              nextButton.addEventListener('click', function() {
                if (currentIndex === radioButtons.length - 1) {
                  currentIndex = 0; // 如果是最后一张图，跳到第一张图
                } else {
                  currentIndex++; // 否则索引加1
                }
                radioButtons[currentIndex].checked = true;
              });
            });
        </script>          
    </head>

    <body>
       <div class="banner-container">
      <input
        type="radio"
        name="radio-set"
        id="banner-control-1"
        checked="checked"
      />
      <input type="radio" name="radio-set" id="banner-control-2" />
      <input type="radio" name="radio-set" id="banner-control-3" />
      <input type="radio" name="radio-set" id="banner-control-4" />
      <input type="radio" name="radio-set" id="banner-control-5" />
      <input type="radio" name="radio-set" id="banner-control-6" />
      <input type="radio" name="radio-set" id="banner-control-7" />
      <input type="radio" name="radio-set" id="banner-control-8" />

      <div class="prev"></div>
      <div class="next"></div>

      <div class="banner-img-container">
        <div class="banner-item" id="banner01">
          <div class="item-img">
            <img
              id="img-banner01"
              src="file/bg-showcase-1.jpg"
              alt="chatbot"
            />
          </div>
          <div class="banner-text">
            <h3>剧本创作</h3>
            <p>根据输入的文本生成剧本</p>
            <p>个性化写作助手</p>
          </div>
        </div>
        <div class="banner-item" id="banner02">
          <div class="item-img">
            <img
              id="img-banner02"
              src="https://github.com/esas4/aigc_web_ui/blob/main/img_voice_synthesis.png?raw=true"
              alt="summary"
            />
          </div>
          <div class="banner-text">
            <h3>语音合成</h3>
            <p>根据输入文本生成语音</p>
            <p>多种角色语音</p>
            <p>自定义语音</p>
          </div>
        </div>
        <div class="banner-item" id="banner03">
          <div class="item-img">
            <img
              id="img-banner03"
              src="https://github.com/esas4/aigc_web_ui/blob/main/img_knowledge_base_Q&A.png?raw=true"
              alt="Q&A"
            />
          </div>
          <div class="banner-text">
            <h3>本地知识库问答</h3>
            <p>上传本地PDF文件</p>
            <p>提供精确的问题回答</p>
          </div>
        </div>
        <div class="banner-item" id="banner04">
          <div class="item-img">
            <img
              id="img-banner04"
              src="https://github.com/esas4/aigc_web_ui/blob/main/img_dh_production.png?raw=true"
              alt="3D animation"
            />
          </div>
          <div class="banner-text">
            <h3>动画数字人制作</h3>
            <p>输入语音，编辑数字人嘴型</p>
          </div>
        </div>
        <div class="banner-item" id="banner05">
          <div class="item-img">
            <img
              id="img-banner05"
              src="https://github.com/esas4/aigc_web_ui/blob/main/img_dClone_production.png?raw=true"
              alt="3D avatar"
            />
          </div>
          <div class="banner-text">
            <h3>3D数字分身</h3>
            <p>上传视频，获得高质量数字分身</p>
            <p>自定义语音驱动</p>
            <p>定制属于自己的分身</p>
          </div>
        </div>
        <div class="banner-item" id="banner06">
          <div class="item-img">
            <img
              id="img-banner06"
              src="https://github.com/esas4/aigc_web_ui/blob/main/img_animation.png?raw=true"
              alt="anime production"
            />
          </div>
          <div class="banner-text">
            <h3>动画制作</h3>
            <p>合成任意人物的动作动画</p>
            <p>多种默认动作</p>
            <p>自定义动作</p>
          </div>
        </div>
        <div class="banner-item" id="banner07">
          <div class="item-img">
            <img
              id="img-banner07"
              src="https://github.com/esas4/aigc_web_ui/blob/main/img_change_cloth.png?raw=true"
              alt="conveniently change cloth"
            />
          </div>
          <div class="banner-text">
            <h3>一键换衣</h3>
            <p>虚拟换衣</p>
          </div>
        </div>
        <div class="banner-item" id="banner08">
          <div class="item-img">
            <img
              id="img-banner08"
              src="https://github.com/esas4/aigc_web_ui/blob/main/img_video_change_face.png?raw=true"
              alt="edit video"
            />
          </div>

          <div class="banner-text">
            <h3>视频编辑</h3>
            <p>替换人脸</p>
          </div>
        </div>
      </div>
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