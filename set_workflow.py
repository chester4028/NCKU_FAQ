#coding:utf-8
import template_json

def set_temp(payload, recipient_id):  # simple wrapper for logging to stdout on heroku

    if payload == 'START_STATE_NO' :
        faq = template_json.Template_json(recipient_id,template_type=2,
              text = "請問是自己的電腦嗎?", payload_yes = "OWNER_YES", payload_no = "OWNER_NO" )

    elif payload == 'START_STATE_YES' :
        faq = template_json.Template_json(recipient_id,template_type=2,
              text = "請問是在自己的座位上嗎?", payload_yes = "ACC_OWN_SEAT_YES", payload_no = "ACC_OWN_SEAT_NO" )

    elif payload == 'ACC_OWN_SEAT_NO' :
        faq = template_json.Template_json(recipient_id,template_type=3,
              text = "請用您自己的學號及密碼於宿網管理系統申請臨時使用", payload_yes = "GOT_IT", payload_no = "ROLL_BACK" )

    elif payload == 'ACC_OWN_SEAT_YES' :
        faq = template_json.Template_json(recipient_id,template_type=2,
              text = "請問正在使用的電腦是註冊時的電腦嗎?", payload_yes = "REG_YES", payload_no = "REG_NO" )

    elif payload == 'REG_YES' :
        faq = template_json.Template_json(recipient_id,template_type=3,
              text = "請使用自動取得IP和DNS，取消Proxy設定和VPN設定，關閉防毒軟體\n如果還是無法連上宿網管理系統，請聯絡計算機中心(61010)", payload_yes = "GOT_IT", payload_no = "ROLL_BACK" )

    elif payload == 'REG_NO' :
        faq = template_json.Template_json(recipient_id,template_type=2,
              text = "請問這台電腦是臨時使用還是未來需要長期使用?", payload_yes = "TEMP_YES", payload_no = "TEMP_NO" )

    elif payload == 'TEMP_YES' :
        faq = template_json.Template_json(recipient_id,template_type=3,
              text = "請用您自己的學號及密碼於宿網管理系統申請臨時使用", payload_yes = "GOT_IT", payload_no = "ROLL_BACK" )

    elif payload == 'TEMP_NO' :
        faq = template_json.Template_json(recipient_id,template_type=3,
              text = "請使用您自己的學號及密碼於宿網管理系統申請變更裝置", payload_yes = "GOT_IT", payload_no = "ROLL_BACK" )

    elif payload == 'OWNER_YES' :
        faq = template_json.Template_json(recipient_id,template_type=2,
              text = "請問是在自己的座位上嗎?", payload_yes = "OWN_SEAT_YES", payload_no = "OWN_SEAT_NO" )

    elif payload == 'OWNER_NO' :
        faq = template_json.Template_json(recipient_id,template_type=3,
              text = "請使用自己的電腦註冊喔", payload_yes = "GOT_IT", payload_no = "ROLL_BACK" )

    elif payload == 'OWN_SEAT_YES' :
        faq = template_json.Template_json(recipient_id,template_type=2,
              text = "請問可以連上宿舍網路管理系統嗎? (http://dorm.cc.ncku.edu.tw/)", payload_yes = "DORM_SITE_YES", payload_no = "DORM_SITE_NO" )

    elif payload == 'OWN_SEAT_NO' :
        faq = template_json.Template_json(recipient_id,template_type=3,
              text = "請在自己的座位上註冊喔", payload_yes = "GOT_IT", payload_no = "ROLL_BACK" )

    elif payload == 'DORM_SITE_YES' :
        faq = template_json.Template_json(recipient_id,template_type=3,
              text = "請點選新使用者登錄，輸入學號及驗證碼登入", payload_yes = "GOT_IT", payload_no = "ROLL_BACK" )

    elif payload == 'DORM_SITE_NO' :
        faq = template_json.Template_json(recipient_id,template_type=3,
              text = "請使用自動取得IP和DNS，取消Proxy設定和VPN設定，關閉防毒軟體\n如果還是無法連上宿網管理系統，請聯絡計算機中心(61010)", payload_yes = "GOT_IT", payload_no = "ROLL_BACK" )

    else :
        faq = template_json.Template_json(recipient_id,template_type=2,
              text = "請在自己的座位上註冊喔", payload_yes = "GOT_IT", payload_no = "ROLL_BACK" )

    return faq
