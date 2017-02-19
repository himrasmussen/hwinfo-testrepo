'''
'''



import helpers
import graph_maker

#TODO: So you'd need vcore, dram voltage, anything with a + in front of it such as +5v

def main(csv_data):
    message = ''


    parameter = "+3.3V [V]"
    try:
        data = csv_data[parameter]
    except KeyError:
        message += helpers.no_key(parameter)
    else:
        message += helpers.check_max_parameter(parameter, csv_data, max_value=3.47)
        message += helpers.check_min_parameter(parameter, csv_data, min_value=3.14)
        image_path = graph_maker.draw_chart(data, parameter)
        message += helpers.html_formatted_image(image_path)
        #message += helpers.check_ripple(parameter, csv_data)

    parameter = "+5V [V]"
    try:
        data = csv_data[parameter]
    except KeyError:
        message += helpers.no_key(parameter)
    else:
        message += helpers.check_max_parameter(parameter, csv_data, max_value=5.25)
        message += helpers.check_min_parameter(parameter, csv_data, min_value=4.75)
        image_path = graph_maker.draw_chart(data, parameter)
        message += helpers.html_formatted_image(image_path)
        #message += helpers.check_ripple(parameter, csv_data)

    parameter = "+12V [V]"
    try:
        data = csv_data[parameter]
    except KeyError:
        message += helpers.no_key(parameter)
    else:
        message += helpers.check_max_parameter(parameter, csv_data, max_value=12.60)
        message += helpers.check_min_parameter(parameter, csv_data, min_value=11.40)
        image_path = graph_maker.draw_chart(data, parameter)
        message += helpers.html_formatted_image(image_path)
        #message += helpers.check_ripple(parameter, csv_data)


    try:
        _3v_relative = helpers.make_rel_dev_list(csv_data["+3.3V [V]"])
        _5_relative = helpers.make_rel_dev_list(csv_data["+5V [V]"])
        _12v_relative = helpers.make_rel_dev_list(csv_data["+12V [V]"])

    except KeyError:
        message += "No data for the tripple graph.\n"
    else:
        da_list = [_3v_relative, _5_relative, _12v_relative]
        image_path = graph_maker.draw_multiple_lines(da_list)
        message += helpers.html_formatted_image(image_path)


    return helpers.sort_message(message)
