import maec_bundle_3_0 as maecbundle
import cybox.win_file_object_1_3 as cybox_win_file_object
import cybox.file_object_1_3 as cybox_file_object
import cybox.uri_object_1_2 as cybox_uri_object

class win_file_object:
    def __init__(self, id):
        self.id = id
        
    def build_object(self, win_file_attributes):
        cybox_object = maecbundle.cybox_core_1_0.AssociatedObjectType(id=self.generator.generate_obj_id())
        fileobj = cybox_win_file_object.WindowsFileObjectType()
        fileobj.set_anyAttributes_({'xsi:type' : 'WinFileObj:WindowsFileObjectType'})
        cybox_object.set_type('File')
        fs_hashes = maecbundle.cybox_common_types_1_0.HashListType()
        for key, value in win_file_attributes.items():
            if key == 'md5' and self.__value_test(value):
                hash_value = maecbundle.cybox_common_types_1_0.HexBinaryObjectAttributeType(datatype='hexBinary', valueOf_=maecbundle.quote_xml(value))
                hash_type = maecbundle.cybox_common_types_1_0.HashNameType(datatype='String', valueOf_='MD5')
                hash = maecbundle.cybox_common_types_1_0.HashType(Simple_Hash_Value=hash_value, Type=hash_type)
                fs_hashes.add_Hash(hash)
            elif key == 'sha1' and self.__value_test(value):
                hash_value = maecbundle.cybox_common_types_1_0.HexBinaryObjectAttributeType(datatype='hexBinary', valueOf_=maecbundle.quote_xml(value))
                hash_type = maecbundle.cybox_common_types_1_0.HashNameType(datatype='String', valueOf_='SHA1')
                hash = maecbundle.cybox_common_types_1_0.HashType(Simple_Hash_Value=hash_value, Type=hash_type)
                fs_hashes.add_Hash(hash)
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
            elif key == 'origin' and self.__value_test(value):
                uriobj = cybox_uri_object.URIObjectType()
                uriobj.set_anyAttributes_({'xsi:type' : 'URIObj:URIObjectType'})
                uriobj.set_Value(maecbundle.cybox_common_types_1_0.AnyURIObjectAttributeType(datatype='AnyURI', valueOf_=maecbundle.quote_xml(value)))
                related_objects = maecbundle.cybox_core_1_0.RelatedObjectsType()
                related_object = maecbundle.cybox_core_1_0.RelatedObjectType(id=self.generator.generate_obj_id(), type_='URI')
                related_object.set_Defined_Object(uriobj)
                related_objects.add_Related_Object(related_object)
                cybox_object.set_Related_Objects(related_objects)
            elif key == 'linkname' and self.__value_test(value):
                sym_links = cybox_file_object.SymLinksListType()
                sym_link = maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_=maecbundle.quote_xml(value))
                sym_links.add_Sym_Link(sym_link)
                fileobj.set_Sym_Links(sym_links)
            elif key == 'controlcode' and self.__value_test(value):
                send_control_effect = maecbundle.cybox_core_1_0.SendControlCodeEffectType(effect_type='ControlCode_Sent', Control_Code=value)
                send_control_effect.set_extensiontype_('cybox:SendControlCodeEffectType')
                cybox_object.set_Defined_Effect(send_control_effect)
            elif key == 'related_object' and value is not None:
                related_objects = maecbundle.cybox_core_1_0.RelatedObjectsType()
                related_objects.add_Related_Object(value)
                cybox_object.set_Related_Objects(related_objects)
            #elif key == 'file_attributes':
            #    file_attributes = win_file_object.WindowsFileAttributesType()
            #    for file_attribute in value:
            #        attribute = win_file_object.WindowsFileAttributeType(datatype='String', valueOf_=file_attribute)
            #        file_attributes.add_Attribute(attribute)
            #    if file_attributes.hasContent_():
            #        fileobj.set_File_Attributes_List(file_attributes)
            elif key == 'effect':
                effect = self.__create_data_effect(value, value.get('type'))
                if effect != None and effect.hasContent_():
                    cybox_object.set_Defined_Effect(effect)
            elif key == 'association':
                cybox_object.set_association_type(value)
                
        if fs_hashes.hasContent_():
            fileobj.set_Hashes(fs_hashes)
        
        if fileobj.hasContent_():
            cybox_object.set_Defined_Object(fileobj)

        return cybox_object