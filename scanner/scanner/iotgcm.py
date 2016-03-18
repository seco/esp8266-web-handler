from gcm import GCM

################################################################################
# GCM INIT
################################################################################
API_KEY = "AIzaSyAh1LQr0p_0qB6b4RKhrMr_nxPtjxZfqiI"

def send_message(reg_id_list, message):
    gcm = GCM(API_KEY)
    data = {'the_message': message}

    print "Received %s" % reg_id_list
    # Downstream message using JSON request
    response = gcm.json_request(registration_ids=reg_id_list, data=data)

    # Downstream message using JSON request with extra arguments
    #res = gcm.json_request(
    #            registration_ids=reg_ids, data=data,
    #                collapse_key='uptoyou', delay_while_idle=True, time_to_live=3600
    #                )

    # Topic Messaging
    #topic = 'topic name'
    #gcm.send_topic_message(topic=topic, data=data)
