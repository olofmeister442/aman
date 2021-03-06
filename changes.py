To Add 

--------------------------------------------------------------------------------

Engine --- Views.py

from OpenAuthApp.models import *

class VerifyMPINAPIView(APIView):
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)

    def get(self, request):        
        data = request.GET
        message = data.get('message')
        alexa_id = data.get('alexa_id')
        device_id = data.get('device_id')
        access_token = data.get('access_token')
        #user = get_user_from_access_token(access_token)
        user = CustomUser.objects.get(username="12312311")
        print(user)
        success = user.check_password(message)
        print(success)

        data = {}
        if success:
            data["response"] = "Verified"
        else:
            data["response"] = None
        return Response(data=data)

VerifyMPIN = VerifyMPINAPIView.as_view()

--------------------------------------------------------------------------------

OpenAuthApp --- init.js

--------------------------------------------------------------------------------
Inside - $('#SUBMIT_TRANSACTION').click(function(){    
var val1 = $(".mobnumber")[0].value;
    var val2 = $(".mobnumber")[1].value;
    var val3 = $(".mobnumber")[2].value;

    $.ajax({
           url: "/chat/VerifyGRID/",
           type: "POST",
           data: {
            val1: val1,
            val2: val2,
            val3: val3,
           },
           success: function(response) {
               if(response["success"]=="1"){
                    window.location.href = unescape(window.location.href.substring(window.location.href.indexOf("next=")+5,));
               }
               else{
                    //Show error message.
               }
           },
           error: function(xhr, textstatus, errorthrown) {
               console.log("Please report this error: "+errorthrown+xhr.status+xhr.responseText);
           }
       });
--------------------------------------------------------------------------------

Engine --- utils.py

--------------------------------------------------------------------------------

do_api_call

try:
    success = answer["success"]
    message = answer["message"]
except:
    success = "true"

if success == "false":
    return (message, "quittree")

process_any_tree_with_stages_new

if choice == "quittree":
    json = {}
    json["is_typable"] = "true"    
    message = message.replace("@","-")                
    json["response"] = message
    json["is_answer"] = "true"
    json["pipe"] = pipe_temp
    clear_data_from_model(user_id)
    reset_user(user_id)                        
    return json

parse_api

try:
    success = answer["success"]
    message = answer["message"]
except:
    success = "true"

if success == "false":
    return (message, success)

Return true for everything below.

parse_sentence

sentence = current_answer
sentence = parse_custom(sentence, user_id)
sentence = parse_is_typable(sentence, user_id)
(sentence, dict_temp) = parse_json(sentence, file, user_id)
sentence = replace_values(sentence, dict_temp)
(sentence, success) = parse_api(sentence, user_id, alexa_id, device_id, access_token)
print("SAAAAAAAAAAAA", sentence, success)
#sentence = replace_if_statement(sentence
#sentence = parse_custom(sentence, user_id)
return (sentence.strip(), success)

create_data_flow

try:
    logger.info("Entered create_data_flow")
    json = {}
    if tree.question_entity_type.entity_group.is_typable:
        json["is_typable"] = "true"
    if tree.question_entity_type.entity_group.is_clickable:
        json["is_clickable"] = "true"
    if tree.question_entity_type.entity_group.is_date:
        json["is_date"] = True
    if tree.question_entity_type.entity_group.is_checkbox:
        json["is_checkbox"] = True        
    (json["response"], success) = parse_sentence(get_question(
        tree, channel), get_question_file(tree, channel), user_id, alexa_id, device_id, access_token)        
    json["response_id"] = get_question_id(tree, channel)        
    if Profile.objects.get(user_id=user_id).re_question:
        if tree.question_entity_type.re_question is not None:
            (json["response"], success) = parse_sentence(get_re_question(
                tree, channel), get_re_question_file(tree, channel), user_id, alexa_id, device_id, access_token)        
    json["choices"] = create_choice_list(
        tree.question_entity_type.entity_group)
    if success == "true":
        json["is_answer"] = "false"
    else:
        json["is_answer"] = "true"
        clear_data_from_model(user_id)
        reset_user(user_id)    
    json["pipe"] = pipe_temp
    json["response"] = json["response"].replace("@","-")        
    return json
except Exception as e:
    print("EEE: ", str(e) )
    logger.error("Error create_data_flow() %s", str(e))

create_data_answer

try:
    logger.info("Entered create_data_answer")
    json = {}
    user = Profile.objects.get(user_id=user_id)
    save_analytics(user)
    json["is_typable"] = "true"
    (json["response"], success) = parse_sentence(get_answer(
        tree, channel), get_file(tree, channel), user_id, alexa_id, device_id, access_token)
    (upvote_link, downvote_link) = create_upvote_downvote_links(user)
    json["upvote_link"] = upvote_link
    json["downvote_link"] = downvote_link
    json["is_answer"] = "true"
    json["recommended_queries"] = get_recommendations(user)
    json["response"] = json["response"].replace("@","-")
    clear_data_from_model(user_id)
    reset_user(user_id)
    return json
except Profile.DoesNotExist:
    logger.error("No matching profile found")
except Exception as e:
    logger.error("Error create_data_answer() %s", str(e))

--------------------------------------------------------------------------------

OpenAuthApp - models.py

--------------------------------------------------------------------------------

unique_1 = models.TextField(null=True,
                            blank=True)

unique_2 = models.TextField(null=True,
		                    blank=True)

--------------------------------------------------------------------------------

urls.py

--------------------------------------------------------------------------------

    url(r'^VerifyGrid', views.VerifyGrid),

--------------------------------------------------------------------------------

views.py:

class VerifyGridAPIView(APIView):
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)

    def post(self, request):        
        data = request.data

        val1 = data.get('val1')
        val2 = data.get('val2')
        val3 = data.get('val3')

        mobile_number = request.user.username
        #account_number = request.user.user_params some parsing and try if current user is super user or what.

        response = get_grid_response(mobile_number, account_number, val1, val2, val3)

        data = {}
        data["success"] = "1"
        return Response(data=data)

VerifyGrid = VerifyGridAPIView.as_view()

--------------------------------------------------------------------------------

apis.py

def get_grid_response(mobile_number, account_number, val1, val2, val3):
    user_id = get_user_id(mobile_number)
    #user_id = "1212"
    input_query = """<XML>
			    <ProcCode>plugin5001</ProcCode>
			    <MessageType>1200</MessageType>
			    <DeliveryChannelCtrlId>RIB</DeliveryChannelCtrlId>
			    <LocalDateTimeStamp>20150315130211</LocalDateTimeStamp>
			    <STAN>202304</STAN>
			    <inputtype>A</inputtype>
			    <input>660160003894</input>
			<validation>
			    <value offset="13">3</value>
			    <value offset="14">2</value>
			    <value offset="15">0</value>
			    <value offset="16">9</value>
			    <value offset="21">5</value>
			    <value offset="22">2</value>
			</validation>
			 <REMARK></REMARK>
			</XML>"""

    #response = call_api(input_query)
    #print(response)
    #account_numbers = parse_account_numbers(response)
    
    return account_numbers
-----------------------------------------------------------------------------
	
	OTP Service Updation
	1) For registration
   <CHANNEL>5</CHANNEL>
  <APPLICATION_NAME>67</APPLICATION_NAME>
  <TRANSACTION_CODE>127</TRANSACTION_CODE>
 
  2) For Online purchase:
   <CHANNEL>5</CHANNEL>
  <APPLICATION_NAME>67</APPLICATION_NAME>
<TRANSACTION_CODE>128</TRANSACTION_CODE>

Live eOTP webservice URL: http://10.50.81.32:9001/OTPEngine/services/OTPWebService?wsdl
