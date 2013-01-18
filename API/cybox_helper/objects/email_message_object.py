import common_methods
import cybox.cybox_common_types_1_0 as cybox_common
import cybox.email_message_object_1_2 as cybox_email_object
import cybox_helper.objects.file_object.file_object as cybox_file_helper
import cybox_helper.objects.uri_object.uri_object as cybox_uri_helper
import cybox_helper.objects.address_object.address_object as cybox_address_helper

class email_object(object):
    def __init__(self):
        pass
    
    @classmethod
    def create_from_dict(cls, email_attributes):
        emailobj = cybox_email_object.EmailMessageObjectType()
        emailobj.set_anyAttributes_({'xsi:type' : 'EmailMessageObj:EmailMessageObjectType'})
        for key, value in email_attributes.items():
            if key == 'attachments':
                attachments = cybox_email_object.AttachmentsType()
                for filedict in value:
                    attachments.add_File(cybox_file_helper.create_from_dict(filedict))
                emailobj.set_Attachments(attachments)
            if key == 'links':
                links = cybox_email_object.LinksType()
                for uridict in value:
                    links.add_Link(cybox_uri_helper.create_from_dict(uridict))
                emailobj.set_Links(links)
            if key == 'header':
                header = cybox_email_object.EmailHeaderType()
                for headername, headervalue in value.items():
                    if headername == 'to':
                        to_list = cybox_email_object.EmailRecipientsType()
                        for addr in headervalue:
                            to_list.add_Recipient(cybox_address_helper.create_from_dict(addr))
                        header.set_To(to_list)
                    if headername == 'cc':
                        cc_list = cybox_email_object.EmailRecipientsType()
                        for addr in headervalue:
                            cc_list.add_Recipient(cybox_address_helper.create_from_dict(addr))
                        header.set_CC(cc_list)
                    if headername == 'bcc':
                        bcc_list = cybox_email_object.EmailRecipientsType()
                        for addr in headervalue:
                            bcc_list.add_Recipient(cybox_address_helper.create_from_dict(addr))
                        header.set_BCC(bcc_list)
                    if headername == 'from':
                        header.set_From(cybox_address_helper.create_from_dict(headervalue))
                    if headername == 'subject':
                        header.set_Subject(common_methods.create_element_from_dict(cybox_common.StringObjectAttributeType(datatype="String"), headervalue))
                    if headername == 'in_reply_to':
                        header.set_In_Reply_To(common_methods.create_element_from_dict(cybox_common.StringObjectAttributeType(datatype="String"), headervalue))
                    if headername == 'message_id':
                        header.set_Message_ID(common_methods.create_element_from_dict(cybox_common.StringObjectAttributeType(datatype="String"), headervalue))
                    if headername == 'date':
                        header.set_From(common_methods.create_element_from_dict(cybox_common.StringObjectAttributeType(datatype="String"), headervalue))
                    if headername == 'sender':
                        header.set_Sender(cybox_address_helper.create_from_dict(headervalue))
                    if headername == 'reply_to':
                        header.set_Reply_To(cybox_address_helper.create_from_dict(headervalue))
                    if headername == 'errors_to':
                        header.set_Errors_To(common_methods.create_element_from_dict(cybox_common.StringObjectAttributeType(datatype="String"), headervalue))
                emailobj.set_Header(header)
            if key == 'optional_header':
                header = cybox_email_object.EmailHeaderType()
                for headername, headervalue in value.items():
                    if headername == 'boundary':
                        header.set_Message_ID(common_methods.create_element_from_dict(cybox_common.StringObjectAttributeType(datatype="String"), headervalue))
                    if headername == 'content_type':
                        header.set_Message_ID(common_methods.create_element_from_dict(cybox_common.StringObjectAttributeType(datatype="String"), headervalue))
                    if headername == 'mime_version':
                        header.set_Message_ID(common_methods.create_element_from_dict(cybox_common.StringObjectAttributeType(datatype="String"), headervalue))
                    if headername == 'precedence':
                        header.set_Message_ID(common_methods.create_element_from_dict(cybox_common.StringObjectAttributeType(datatype="String"), headervalue))
                    if headername == 'x_mailer':
                        header.set_Message_ID(common_methods.create_element_from_dict(cybox_common.StringObjectAttributeType(datatype="String"), headervalue))
                    if headername == 'x_originating_ip':
                        header.set_Message_ID(cybox_address_helper.create_from_dict(headervalue))
                    if headername == 'x_priority':
                        header.set_Message_ID(common_methods.create_element_from_dict(cybox_common.PositiveIntegerObjectAttributeType(datatype="PositiveInt"), headervalue))
                emailobj.set_Optional_Header(header)
            if key == 'raw_header' and common_methods.test_value(value):
                emailobj.set_Raw_Header(common_methods.create_element_from_dict(cybox_common.StringObjectAttributeType(datatype='String'),value))
            if key == 'raw_body' and common_methods.test_value(value):
                emailobj.set_Raw_Body(common_methods.create_element_from_dict(cybox_common.StringObjectAttributeType(datatype='String'),value))
            elif key == 'email_server' and common_methods.test_value(value):
                emailobj.set_Email_Server(common_methods.create_element_from_dict(cybox_common.StringObjectAttributeType(datatype='String'),value))
        return emailobj

    @classmethod
    def parse_into_dict(cls, defined_object, defined_object_dict = None):
        if defined_object_dict == None:
            defined_object_dict = {}
            
        if defined_object.get_Raw_Body() is not None:
            defined_object_dict['raw_body'] = common_methods.parse_element_into_dict(defined_object.get_Raw_Body())
        if defined_object.get_Raw_Header() is not None:
            defined_object_dict['raw_header'] = common_methods.parse_element_into_dict(defined_object.get_Raw_Header())
        if defined_object.get_Email_Server() is not None:
            defined_object_dict['email_server'] = common_methods.parse_element_into_dict(defined_object.get_Email_Server())
        return defined_object_dict


