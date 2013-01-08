import cybox.cybox_core_1_0 as cybox # bindings
import cybox.cybox_common_types_1_0 as cybox_common # bindings
from objects.address_object import address_object 
from objects.uri_object import uri_object
from objects.port_object import port_object
from objects.http_session_object import http_session_object
from objects.network_connection_object import network_connection_object
from objects.network_packet_object import network_packet_object

class cybox_core(object):
    def __init__(self):
        pass
    
    @classmethod
    def create_observables_from_dict(cls, observables_dict):
        pass

    #Parse the observables into a dictionary-esque representation
    @classmethod
    def parse_observables_into_dict(cls, observables):
        observables_list = []
        for observable in observables.get_Observable():
            observables_list.append(cls.parse_observable_into_dict(observable))
        return observables_list

    @classmethod
    def parse_observable_into_dict(cls, observable):
        observable_dict = {}
        if observable.get_id() is not None:
            observable_dict['id'] = observable.get_id()
        if observable.get_idref() is not None:
            observable_dict['idref'] = observable.get_idref()
        if observable.get_Title() is not None:
            observable_dict['title'] = observable.get_Title()
        if observable.get_Description() is not None:
            observable_dict['description'] = cls.parse_structured_text_type_into_dict(observable.get_Description())
        if observable.get_Stateful_Measure() is not None:
            observable_dict['stateful_measure'] = cls.parse_stateful_measure_into_dict(observable.get_Stateful_Measure())
        #TODO - add rest of observable components
        return observable_dict

    #Parse and return a dictionary for a stateful measure
    @classmethod
    def parse_stateful_measure_into_dict(cls, stateful_measure):
        stateful_measure_dict = {}
        if stateful_measure.get_name() is not None:
            stateful_measure_dict['name'] = stateful_measure.get_Name()
        if stateful_measure.get_has_changed() is not None:
            stateful_measure_dict['has_changed'] = stateful_measure.get_has_changed()
        if stateful_measure.get_Description() is not None:
            stateful_measure_dict['description'] = cls.parse_structured_text_type_into_dict(stateful_measure.get_Description())
        if stateful_measure.get_Object() is not None:
            stateful_measure_dict['object'] = cls.parse_object_into_dict(stateful_measure.get_Object())
        return stateful_measure_dict

    #Parse and return a dictionary for an object
    @classmethod
    def parse_object_into_dict(cls, object):
        object_dict = {}
        if object.get_id() is not None:
            object_dict['id'] = object.get_id()
        if object.get_idref() is not None:
            object_dict['idref'] = object.get_idref()
        if object.get_type() is not None:
            object_dict['type'] = object.get_type()
        if object.get_object_state() is not None:
            object_dict['object_state'] = object.get_object_state()
        if object.get_Description() is not None:
            object_dict['description'] = cls.parse_structured_text_type_into_dict(object.get_Description())
        if object.get_Defined_Object() is not None:
            object_dict['defined_object'] = cls.parse_defined_object_into_dict(object.get_Defined_Object())
        #TODO - add rest of object components
        return object_dict

    @classmethod
    def parse_structured_text_type_into_dict(cls, element):
        structured_text_dict = {}
        if element.get_Text_Title() is not None and len(element.get_Text_Title()) > 0:
            text_titles = []
            for text_title in element.get_Text_Title():
                text_titles.append(text_title)
            structured_text_dict['text_title'] = text_titles
        if element.get_Text() is not None and len(element.get_Text()) > 0:
            texts = []
            for text in element.get_Text():
                texts.append(text)
            structured_text_dict['text'] = texts
        if element.get_Code_Example_Language() is not None and len(element.get_Code_Example_Language()) > 0:
            code_example_languages = []
            for code_example_language in element.get_Code_Example_Language():
                code_example_languages.append(code_example_language)
            structured_text_dict['code_example_language'] = code_example_languages
        if element.get_Code() is not None and len(element.get_Code()) > 0:
            codes = []
            for code in element.get_Code():
                codes.append(code)
            structured_text_dict['code'] = codes
        if element.get_Comment() is not None and len(element.get_Comment()) > 0:
            comments = []
            for comment in element.get_Comment():
                comments.append(comment)
            structured_text_dict['comment'] = comments
        if element.get_Images() is not None:
            images = []
            for image in element.get_Images().get_Image():
                image_dict = {}
                if image.get_Image_Location() is not None: image_dict['image_location'] = image.get_Image_Location()
                if image.get_Image_Title() is not None: image_dict['image_title'] = image.get_Image_Title()
                images.append(image_dict)
            structured_text_dict['images'] = images
        if element.get_Block() is not None: structured_text_dict['block'] = cls.parse_structured_text_type_into_dict(element.get_Block())
        return structured_text_dict

    #Parse and return a dictionary for a defined object
    @classmethod
    def parse_defined_object_into_dict(cls, defined_object):
        defined_object_dict = {}
        any_attributes = defined_object.get_anyAttributes_()
        for key, value in any_attributes.items():
            if key == '{http://www.w3.org/2001/XMLSchema-instance}type':
                type_value = value.split(':')[1]
                defined_object_dict['xsi:type'] = type_value
                object_type = cybox.defined_objects.get(type_value).get('binding_name').split('_object')[0] + '_object'
                defined_object_dict['object_type'] = object_type
                object_api = globals().get(object_type)
                try:
                    return getattr(object_api, 'parse_into_dict')(defined_object, defined_object_dict)
                except AttributeError:
                    return defined_object_dict