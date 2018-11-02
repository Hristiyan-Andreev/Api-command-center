import requests as req
import dicttoxml
import ijson

def list_live_events(elemental_ip):
	endpoint = '/api/live_events/'
	headers = {'Accept': 'application/xml', 'Content-type': 'application/xml'}
	
	url = 'http://' + elemental_ip + endpoint
	print(url)
	response = req.get(url, headers)
	return response.status_code
	
def start_cue_point(elemental_ip, stream_id):
	endpoint = '/api/live_events/' + stream_id + '/cue_point/'
	myheaders = {'Accept': 'application/xml', 'Content-type': 'application/xml'}
	body = {
			'cue_point':{
			'event_id': stream_id,
			'splice_offset': '0',
			'duration': '0'	
						}
			}
	bodyxml = dicttoxml.dicttoxml(body, root=False, attr_type=False)
	url = 'http://' + elemental_ip + endpoint
	
	response = req.post(url, headers = myheaders, data = bodyxml)
		
	#return str(response.status_code)
	return response.text
	

def stop_cue_point(elemental_ip, stream_id):
	endpoint = '/api/live_events/' + stream_id + '/cue_point/'
	myheaders = {'Accept': 'application/xml', 'Content-type': 'application/xml'}
	body = {
			'cue_point':{
			'event_id': stream_id,
			'return_offset': 0
						}
			}
	bodyxml = dicttoxml.dicttoxml(body, root=False, attr_type=False)
	url = 'http://' + elemental_ip + endpoint
	response = req.post(url, headers = myheaders, data = bodyxml)
	
	return response.text
	#return response
	
def main():
	elemental_ip = '37.157.142.3'
	#list_live_events(elemental_ip)
	#start_cue_point(elemental_ip, '17')
	stop_cue_point(elemental_ip, '17')
if __name__ == "__main__":
	main()