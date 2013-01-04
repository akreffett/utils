
def parse_element_into_dict(element):
    element_dict = {}
    if element.get_id() is not None: element_dict['id'] = element.get_id()
    if element.get_idref() is not None: element_dict['idref'] = element.get_idref()
    if element.get_datatype() is not None: element_dict['datatype'] = element.get_datatype()
    if element.get_condition() is not None: element_dict['condition'] = element.get_condition()
    if element.get_pattern_type() is not None: element_dict['pattern_type'] = element.get_pattern_type()
    if element.get_regex_syntax() is not None: element_dict['regex_syntax'] = element.get_regex_syntax()
    if element.get_start_range() is not None: element_dict['start_range'] = element.get_start_range()
    if element.get_end_range() is not None: element_dict['end_range'] = element.get_end_range()
    if element.get_value_set() is not None: element_dict['value_set'] = element.get_value_set()
    if element.get_has_changed() is not None: element_dict['has_changed'] = element.get_has_changed()
    if element.get_trend() is not None: element_dict['trend'] = element.get_trend()
    if element.get_appears_random() is not None: element_dict['appears_random'] = element.get_appears_random()
    if element.get_is_obfuscated() is not None: element_dict['is_obfuscated'] = element.get_is_obfuscated()
    if element.get_obfuscation_algorithm_ref() is not None: element_dict['obfuscation_algorithm_ref'] = element.get_obfuscation_algorithm_ref()
    if element.get_is_defanged() is not None: element_dict['is_defanged'] = element.get_is_defanged()
    if element.get_defanging_algorithm_ref() is not None: element_dict['defanging_algorithm_ref'] = element.get_defanging_algorithm_ref()
    if element.get_refanging_transform_type() is not None: element_dict['refanging_transform_type'] = element.get_refanging_transform_type()
    if element.get_refanging_transform() is not None: element_dict['refanging_transform'] = element.get_refanging_transform()
    if element.get_valueOf_() is not None: element_dict['value'] = element.get_valueOf_()
    return element_dict

#Test if a value is not None and has a length greater than 0
def test_value(value):
    if value is not None and len(str(value)) > 0:
        return True
    else:
        return False
