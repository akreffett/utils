import maec_bundle_3_0 as maecbundle
import cybox.win_file_object_1_3 as cybox_win_file_object
import cybox.file_object_1_3 as cybox_file_object
import cybox.uri_object_1_2 as cybox_uri_object
import cybox_helper.objects.file_object as file_builder

class win_file_object(file_builder):
    def __init__(self):
        pass
    
    @classmethod
    def create_from_dict(cls, file_attributes):
        fileobj = super(win_file_object, cls).create_from_dict(file_attributes)
        
        for key, value in file_attributes.items():
            pass

    @classmethod
    def parse_into_dict(cls, defined_object, defined_object_dict = None):
        defined_object_dict = super(win_file_object, cls).parse_into_dict(defined_object, defined_object_dict)
        
        