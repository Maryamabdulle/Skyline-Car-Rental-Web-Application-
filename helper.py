def convert_date(date_str):
	from datetime import datetime
	datetime_obj = datetime.strptime(date_str, "%Y-%m-%d")
	return datetime_obj


def compare_dates(date_start, date_end):
	if date_start < date_end:
		return True
	else:
		return False

def convert_datetime(datetime_str):
	from datetime import datetime
	datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
	return datetime_obj


def check_card_expfrmt(var):
	try:
		var = var.split('/')
		if len(var[0]) == 2 and len(var[1]) == 2:
			return True
		else:
			return False
	except:
		return False