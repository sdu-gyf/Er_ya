var fa = $("body");
var btn = $("<li></li>");
var json =
{
    "background": "#31e16d",
    "height": "16px",
    "padding": "5px",
    "z-index": 999999,
    "cursor": "pointer",
    "top": "300px",
    "right": "120px",
    "position": "fixed"
};
btn.css(json);
btn.html("<span id='lfsenior'>�����Զ�����ģʽ</span>");
fa.append(btn);

btn.click(function () {

    setInterval(function () {
        //��ȡiframe
        var video = $("iframe").contents().find("iframe").contents();
        //���ź���
        var play = function () {
            video.find("#video > button").click();
            var jy = video.find("#video > div.vjs-control-bar > div.vjs-volume-panel.vjs-control.vjs-volume-panel-vertical > button");
            if (jy.attr("title") != "ȡ������") {
                jy.click()
            }
        }
        //������ڼ���
        var load = video.find("#loading");
        if (load.css("visibility") != "hidden") {
            return;
        }
        //��ȡ��ǰ����
        var spans = video.find("#video > div.vjs-control-bar > div.vjs-progress-control.vjs-control > div").attr("aria-valuenow");
        // �����û������
        if (spans != 100) {
            play();
        }
        //������Ž���
        //�����л���һ���Զ�����
        if (spans == 100) {
            var bs = false;
            $(".onetoone").find(".flush").each(function () {
                if (bs) {
                    $(this).prev("a").on('click', "#coursetree>ncells", function () {
                        console.log("�ѽ����½ڣ�" + $(this).prev("a").attr("title"))
                    })
                    var str = $(this).prev("a").attr("href");
                    str = str.match(/'(\S*)'/)[1];
                    var reg = new RegExp("'", "g");
                    str = str.replace(reg, "");
                    var href = str.split(",");
                    getTeacherAjax(href[0], href[1], href[2])
                    bs = false;
                }
                if ($(this).css("display") == "block") {
                    bs = true;
                }
            })
        }
        $("#lfsenior").html("�Զ�ģʽ�ѿ���,���½���:" + spans + "%");
    }, 100);

});