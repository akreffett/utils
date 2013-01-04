import maec_bundle_3_0 as maecbundle
import cybox.file_object_1_3 as cybox_file_object

class file_object:
    def __init__(self, id):
        self.id = id
        
    def build_object(self, file_attributes):
        cybox_object = maecbundle.cybox_core_1_0.AssociatedObjectType(id=self.generator.generate_obj_id())
        fileobj = cybox_file_object.FileObjectType()
        fileobj.set_anyAttributes_({'xsi:type' : 'FileObj:FileObjectType'})
        cybox_object.set_type('File')
        fs_hashes = maecbundle.cybox_common_types_1_0.HashListType()
        
        for key, value in file_attributes.items():
            if key == 'md5' and self.__value_test(value):
                hash_value = maecbundle.cybox_common_types_1_0.HexBinaryObjectAttributeType(datatype='hexBinary', valueOf_=maecbundle.quote_xml(value))
                hash_type = maecbundle.cybox_common_types_1_0.HashNameType(datatype='String', valueOf_='MD5')
                hash = maecbundle.cybox_common_types_1_0.HashType(Simple_Hash_Value=hash_value, Type=hash_type)
                fs_hashes.add_Hash(hash)
            elif key == 'sha1' and self.__value_test(value):
                hash_value = maecbundle.cybox_common_types_1_0.HexBinaryObjectAttributeType(datatype='hexBinary', valueOf_=maecbundle.quote_xml(value))
                hash_type = maecbundle.cybox_common_types_1_0.HashNameType(datatype='String', valueOf_='SHA1')
                hash_obj = maecbundle.cybox_common_types_1_0.HashType(Simple_Hash_Value=hash_value, Type=hash_type)
                fs_hashes.add_Hash(hash_obj)
            elif key == 'packer' and self.__value_test(value):
                packer_list = cybox_file_object.PackerListType()
                packer = cybox_file_object.PackerType(Name=maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_=maecbundle.quote_xml(value)))
                packer_list.add_Packer(packer)
                fileobj.set_Packer_List(packer_list)
            elif key == 'av_aliases':
                cybox_object.set_Domain_specific_Object_Attributes(value)
            elif key == 'filename' and self.__value_test(value):
                fileobj.set_File_Name(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_=maecbundle.quote_xml(value)))
            elif key == 'filepath' and self.__value_test(value):
                filepath = maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_=maecbundle.quote_xml(value))
                fileobj.set_File_Path(filepath)

        if fs_hashes.hasContent_():
            fileobj.set_Hashes(fs_hashes)
        
        if fileobj.hasContent_():
            cybox_object.set_Defined_Object(fileobj)

        return cybox_object