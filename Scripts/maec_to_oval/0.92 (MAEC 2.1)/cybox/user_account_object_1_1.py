#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#
# Generated Mon Apr 09 15:34:14 2012 by generateDS.py version 2.7b.
#

import sys
import getopt
import re as re_
import account_object_1_1 as account_object
import common_types_1_0 as common

etree_ = None
Verbose_import_ = False
(   XMLParser_import_none, XMLParser_import_lxml,
    XMLParser_import_elementtree
    ) = range(3)
XMLParser_import_library = None
try:
    # lxml
    from lxml import etree as etree_
    XMLParser_import_library = XMLParser_import_lxml
    if Verbose_import_:
        print("running with lxml.etree")
except ImportError:
    try:
        # cElementTree from Python 2.5+
        import xml.etree.cElementTree as etree_
        XMLParser_import_library = XMLParser_import_elementtree
        if Verbose_import_:
            print("running with cElementTree on Python 2.5+")
    except ImportError:
        try:
            # ElementTree from Python 2.5+
            import xml.etree.ElementTree as etree_
            XMLParser_import_library = XMLParser_import_elementtree
            if Verbose_import_:
                print("running with ElementTree on Python 2.5+")
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree_
                XMLParser_import_library = XMLParser_import_elementtree
                if Verbose_import_:
                    print("running with cElementTree")
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as etree_
                    XMLParser_import_library = XMLParser_import_elementtree
                    if Verbose_import_:
                        print("running with ElementTree")
                except ImportError:
                    raise ImportError("Failed to import ElementTree from any known place")

def parsexml_(*args, **kwargs):
    if (XMLParser_import_library == XMLParser_import_lxml and
        'parser' not in kwargs):
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        kwargs['parser'] = etree_.ETCompatXMLParser()
    doc = etree_.parse(*args, **kwargs)
    return doc

#
# User methods
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ImportError, exp:

    class GeneratedsSuper(object):
        def gds_format_string(self, input_data, input_name=''):
            return input_data
        def gds_validate_string(self, input_data, node, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % input_data
        def gds_validate_integer(self, input_data, node, input_name=''):
            return input_data
        def gds_format_integer_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_integer_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of integers')
            return input_data
        def gds_format_float(self, input_data, input_name=''):
            return '%f' % input_data
        def gds_validate_float(self, input_data, node, input_name=''):
            return input_data
        def gds_format_float_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_float_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of floats')
            return input_data
        def gds_format_double(self, input_data, input_name=''):
            return '%e' % input_data
        def gds_validate_double(self, input_data, node, input_name=''):
            return input_data
        def gds_format_double_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_double_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of doubles')
            return input_data
        def gds_format_boolean(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_boolean(self, input_data, node, input_name=''):
            return input_data
        def gds_format_boolean_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_boolean_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                if value not in ('true', '1', 'false', '0', ):
                    raise_parse_error(node, 'Requires sequence of booleans ("true", "1", "false", "0")')
            return input_data
        def gds_str_lower(self, instring):
            return instring.lower()
        def get_path_(self, node):
            path_list = []
            self.get_path_list_(node, path_list)
            path_list.reverse()
            path = '/'.join(path_list)
            return path
        Tag_strip_pattern_ = re_.compile(r'\{.*\}')
        def get_path_list_(self, node, path_list):
            if node is None:
                return
            tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
            if tag:
                path_list.append(tag)
            self.get_path_list_(node.getparent(), path_list)
        def get_class_obj_(self, node, default_class=None):
            class_obj1 = default_class
            if 'xsi' in node.nsmap:
                classname = node.get('{%s}type' % node.nsmap['xsi'])
                if classname is not None:
                    names = classname.split(':')
                    if len(names) == 2:
                        classname = names[1]
                    class_obj2 = globals().get(classname)
                    if class_obj2 is not None:
                        class_obj1 = class_obj2
            return class_obj1
        def gds_build_any(self, node, type_name=None):
            return None


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = 'ascii'
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')

#
# Support/utility functions.
#

def showIndent(outfile, level):
    for idx in range(level):
        outfile.write('    ')

def quote_xml(inStr):
    if not inStr:
        return ''
    s1 = (isinstance(inStr, basestring) and inStr or
          '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1

def quote_attrib(inStr):
    s1 = (isinstance(inStr, basestring) and inStr or
          '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1

def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1

def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text

def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


class GDSParseError(Exception):
    pass

def raise_parse_error(node, msg):
    if XMLParser_import_library == XMLParser_import_lxml:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline, )
    else:
        msg = '%s (element %s)' % (msg, node.tag, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name, namespace):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip(): 
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(outfile, level, namespace,name)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (self.name, self.value, self.name))
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s", "%s"),\n' % \
                (self.category, self.content_type, self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s", "%s"),\n' % \
                (self.category, self.content_type, self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s",\n' % \
                (self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0):
        self.name = name
        self.data_type = data_type
        self.container = container
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container

def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#

class UserAccountObjectType(account_object.AccountObjectType):
    """The UserAccountObjectType type is intended to characterize generic
    user accounts.The passwordrequired attribute specifies whether a
    password is required for this user account."""
    subclass = None
    superclass = account_object.AccountObjectType
    def __init__(self, disabled=None, locked_out=None, Description=None, Domain=None, password_required=None, User_ID=None, Full_Name=None, Group_List=None, Home_Directory=None, Last_Login=None, Privilege_List=None, Script_Path=None, Username=None, User_Password_Age=None):
        super(UserAccountObjectType, self).__init__(disabled, locked_out, Description, Domain)
        self.password_required = _cast(bool, password_required)
        self.User_ID = User_ID
        self.Full_Name = Full_Name
        self.Group_List = Group_List
        self.Home_Directory = Home_Directory
        self.Last_Login = Last_Login
        self.Privilege_List = Privilege_List
        self.Script_Path = Script_Path
        self.Username = Username
        self.User_Password_Age = User_Password_Age
    def factory(*args_, **kwargs_):
        if UserAccountObjectType.subclass:
            return UserAccountObjectType.subclass(*args_, **kwargs_)
        else:
            return UserAccountObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_User_ID(self): return self.User_ID
    def set_User_ID(self, User_ID): self.User_ID = User_ID
    def get_Full_Name(self): return self.Full_Name
    def set_Full_Name(self, Full_Name): self.Full_Name = Full_Name
    def get_Group_List(self): return self.Group_List
    def set_Group_List(self, Group_List): self.Group_List = Group_List
    def get_Home_Directory(self): return self.Home_Directory
    def set_Home_Directory(self, Home_Directory): self.Home_Directory = Home_Directory
    def get_Last_Login(self): return self.Last_Login
    def set_Last_Login(self, Last_Login): self.Last_Login = Last_Login
    def get_Privilege_List(self): return self.Privilege_List
    def set_Privilege_List(self, Privilege_List): self.Privilege_List = Privilege_List
    def get_Script_Path(self): return self.Script_Path
    def set_Script_Path(self, Script_Path): self.Script_Path = Script_Path
    def get_Username(self): return self.Username
    def set_Username(self, Username): self.Username = Username
    def get_User_Password_Age(self): return self.User_Password_Age
    def set_User_Password_Age(self, User_Password_Age): self.User_Password_Age = User_Password_Age
    def get_password_required(self): return self.password_required
    def set_password_required(self, password_required): self.password_required = password_required
    def export(self, outfile, level, namespace_='UserAccountObj:', name_='UserAccountObjectType', namespacedef_=''):
        showIndent(outfile, level)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='UserAccountObjectType')
        if self.hasContent_():
            outfile.write('>\n')
            self.exportChildren(outfile, level + 1, 'UserAccountObj:', name_)
            showIndent(outfile, level)
            outfile.write('</%s%s>\n' % (namespace_, name_))
        else:
            outfile.write('/>\n')
    def exportAttributes(self, outfile, level, already_processed, namespace_='UserAccountObj:', name_='UserAccountObjectType'):
        super(UserAccountObjectType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='UserAccountObjectType')
        if self.password_required is not None and 'password_required' not in already_processed:
            already_processed.append('password_required')
            outfile.write(' password_required="%s"' % self.gds_format_boolean(self.gds_str_lower(str(self.password_required)), input_name='password_required'))
    def exportChildren(self, outfile, level, namespace_='UserAccountObj:', name_='UserAccountObjectType', fromsubclass_=False):
        if self.User_ID is not None:
            self.User_ID.export(outfile, level, namespace_, name_='User_ID')
        if self.Full_Name is not None:
            self.Full_Name.export(outfile, level, namespace_, name_='Full_Name')
        if self.Group_List is not None:
            self.Group_List.export(outfile, level, namespace_, name_='Group_List')
        if self.Home_Directory is not None:
            self.Home_Directory.export(outfile, level, namespace_, name_='Home_Directory')
        if self.Last_Login is not None:
            self.Last_Login.export(outfile, level, namespace_, name_='Last_Login')
        if self.Privilege_List is not None:
            self.Privilege_List.export(outfile, level, namespace_, name_='Privilege_List')
        if self.Script_Path is not None:
            self.Script_Path.export(outfile, level, namespace_, name_='Script_Path')
        if self.Username is not None:
            self.Username.export(outfile, level, namespace_, name_='Username')
        if self.User_Password_Age is not None:
            self.User_Password_Age.export(outfile, level, namespace_, name_='User_Password_Age')
        super(UserAccountObjectType, self).exportChildren(outfile, level, namespace_, name_, True)
    def hasContent_(self):
        if (
            self.User_ID is not None or
            self.Full_Name is not None or
            self.Group_List is not None or
            self.Home_Directory is not None or
            self.Last_Login is not None or
            self.Privilege_List is not None or
            self.Script_Path is not None or
            self.Username is not None or
            self.User_Password_Age is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='UserAccountObjectType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.password_required is not None and 'password_required' not in already_processed:
            already_processed.append('password_required')
            showIndent(outfile, level)
            outfile.write('password_required = %s,\n' % (self.password_required,))
    def exportLiteralChildren(self, outfile, level, name_):
        if self.User_ID is not None:
            showIndent(outfile, level)
            outfile.write('User_ID=%s,\n' % quote_python(self.User_ID).encode(ExternalEncoding))
        if self.Full_Name is not None:
            showIndent(outfile, level)
            outfile.write('Full_Name=%s,\n' % quote_python(self.Full_Name).encode(ExternalEncoding))
        if self.Group_List is not None:
            showIndent(outfile, level)
            outfile.write('Group_List=model_.GroupListType(\n')
            self.Group_List.exportLiteral(outfile, level, name_='Group_List')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Home_Directory is not None:
            showIndent(outfile, level)
            outfile.write('Home_Directory=%s,\n' % quote_python(self.Home_Directory).encode(ExternalEncoding))
        if self.Last_Login is not None:
            showIndent(outfile, level)
            outfile.write('Last_Login=%s,\n' % quote_python(self.Last_Login).encode(ExternalEncoding))
        if self.Privilege_List is not None:
            showIndent(outfile, level)
            outfile.write('Privilege_List=model_.PrivilegeListType(\n')
            self.Privilege_List.exportLiteral(outfile, level, name_='Privilege_List')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Script_Path is not None:
            showIndent(outfile, level)
            outfile.write('Script_Path=%s,\n' % quote_python(self.Script_Path).encode(ExternalEncoding))
        if self.Username is not None:
            showIndent(outfile, level)
            outfile.write('Username=%s,\n' % quote_python(self.Username).encode(ExternalEncoding))
        if self.User_Password_Age is not None:
            showIndent(outfile, level)
            outfile.write('User_Password_Age=%s,\n' % quote_python(self.User_Password_Age).encode(ExternalEncoding))
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('password_required', node)
        if value is not None and 'password_required' not in already_processed:
            already_processed.append('password_required')
            if value in ('true', '1'):
                self.password_required = True
            elif value in ('false', '0'):
                self.password_required = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'User_ID':
            User_ID_ = common.StringObjectAttributeType.factory()
            User_ID_.build(child_)
            self.User_ID = User_ID_
        elif nodeName_ == 'Full_Name':
            Full_Name_ = common.StringObjectAttributeType.factory()
            Full_Name_.build(child_)
            self.Full_Name = Full_Name_
        elif nodeName_ == 'Group_List':
            obj_ = GroupListType.factory()
            obj_.build(child_)
            self.set_Group_List(obj_)
        elif nodeName_ == 'Home_Directory':
            Home_Directory_ = common.StringObjectAttributeType.factory()
            Home_Directory_.build(child_)
            self.Home_Directory = Home_Directory_
        elif nodeName_ == 'Last_Login':
            Last_Login_ = common.DateTimeObjectAttributeType.factory()
            Last_Login_.build(child_)
            self.Last_Login = Last_Login_
        elif nodeName_ == 'Privilege_List':
            obj_ = PrivilegeListType.factory()
            obj_.build(child_)
            self.set_Privilege_List(obj_)
        elif nodeName_ == 'Script_Path':
            Script_Path_ = common.StringObjectAttributeType.factory()
            Script_Path_.build(child_)
            self.Script_Path = Script_Path_
        elif nodeName_ == 'Username':
            Username_ = common.StringObjectAttributeType.factory()
            Username_.build(child_)
            self.Username = Username_
        elif nodeName_ == 'User_Password_Age':
            User_Password_Age_ = common.DurationObjectAttributeType.factory()
            User_Password_Age_.build(child_)
            self.User_Password_Age = User_Password_Age_
        super(UserAccountObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class UserAccountObjectType


class PrivilegeListType(GeneratedsSuper):
    """The PrivilegeListType type specifies the list of privileges that the
    user account has."""
    subclass = None
    superclass = None
    def __init__(self, Privilege=None):
        if Privilege is None:
            self.Privilege = []
        else:
            self.Privilege = Privilege
    def factory(*args_, **kwargs_):
        if PrivilegeListType.subclass:
            return PrivilegeListType.subclass(*args_, **kwargs_)
        else:
            return PrivilegeListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Privilege(self): return self.Privilege
    def set_Privilege(self, Privilege): self.Privilege = Privilege
    def add_Privilege(self, value): self.Privilege.append(value)
    def insert_Privilege(self, index, value): self.Privilege[index] = value
    def export(self, outfile, level, namespace_='UserAccountObj:', name_='PrivilegeListType', namespacedef_=''):
        showIndent(outfile, level)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='PrivilegeListType')
        if self.hasContent_():
            outfile.write('>\n')
            self.exportChildren(outfile, level + 1, namespace_, name_)
            showIndent(outfile, level)
            outfile.write('</%s%s>\n' % (namespace_, name_))
        else:
            outfile.write('/>\n')
    def exportAttributes(self, outfile, level, already_processed, namespace_='UserAccountObj:', name_='PrivilegeListType'):
        pass
    def exportChildren(self, outfile, level, namespace_='UserAccountObj:', name_='PrivilegeListType', fromsubclass_=False):
        for Privilege_ in self.get_Privilege():
            Privilege_.export(outfile, level, namespace_, name_='Privilege')
    def hasContent_(self):
        if (
            self.Privilege
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='PrivilegeListType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Privilege=[\n')
        level += 1
        for Privilege_ in self.Privilege:
            showIndent(outfile, level)
            outfile.write('model_.PrivilegeType(\n')
            Privilege_.exportLiteral(outfile, level, name_='PrivilegeType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Privilege':
            type_name_ = child_.attrib.get('{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]
                class_ = globals()[type_name_]
                obj_ = class_.factory()
                obj_.build(child_)
            else:
                raise NotImplementedError(
                    'Class not implemented for <Privilege> element')
            self.Privilege.append(obj_)
# end class PrivilegeListType


class PrivilegeType(GeneratedsSuper):
    """The PrivilegeType type specifies a specific privilege that a user
    has. This is an abstract type since user privileges are
    operating-system specific, and is extended as needed in the
    derived CybOX object schemas."""
    subclass = None
    superclass = None
    def __init__(self):
        pass
    def factory(*args_, **kwargs_):
        if PrivilegeType.subclass:
            return PrivilegeType.subclass(*args_, **kwargs_)
        else:
            return PrivilegeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def export(self, outfile, level, namespace_='UserAccountObj:', name_='PrivilegeType', namespacedef_=''):
        showIndent(outfile, level)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='PrivilegeType')
        if self.hasContent_():
            outfile.write('>\n')
            self.exportChildren(outfile, level + 1, namespace_, name_)
            outfile.write('</%s%s>\n' % (namespace_, name_))
        else:
            outfile.write('/>\n')
    def exportAttributes(self, outfile, level, already_processed, namespace_='UserAccountObj:', name_='PrivilegeType'):
        pass
    def exportChildren(self, outfile, level, namespace_='UserAccountObj:', name_='PrivilegeType', fromsubclass_=False):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='PrivilegeType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class PrivilegeType


class GroupListType(GeneratedsSuper):
    """The GroupListType type specifies the groups that the user account
    belongs to."""
    subclass = None
    superclass = None
    def __init__(self, Group=None):
        if Group is None:
            self.Group = []
        else:
            self.Group = Group
    def factory(*args_, **kwargs_):
        if GroupListType.subclass:
            return GroupListType.subclass(*args_, **kwargs_)
        else:
            return GroupListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Group(self): return self.Group
    def set_Group(self, Group): self.Group = Group
    def add_Group(self, value): self.Group.append(value)
    def insert_Group(self, index, value): self.Group[index] = value
    def export(self, outfile, level, namespace_='UserAccountObj:', name_='GroupListType', namespacedef_=''):
        showIndent(outfile, level)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='GroupListType')
        if self.hasContent_():
            outfile.write('>\n')
            self.exportChildren(outfile, level + 1, namespace_, name_)
            showIndent(outfile, level)
            outfile.write('</%s%s>\n' % (namespace_, name_))
        else:
            outfile.write('/>\n')
    def exportAttributes(self, outfile, level, already_processed, namespace_='UserAccountObj:', name_='GroupListType'):
        pass
    def exportChildren(self, outfile, level, namespace_='UserAccountObj:', name_='GroupListType', fromsubclass_=False):
        for Group_ in self.get_Group():
            Group_.export(outfile, level, namespace_, name_='Group')
    def hasContent_(self):
        if (
            self.Group
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='GroupListType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Group=[\n')
        level += 1
        for Group_ in self.Group:
            showIndent(outfile, level)
            outfile.write('model_.GroupType(\n')
            Group_.exportLiteral(outfile, level, name_='GroupType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Group':
            type_name_ = child_.attrib.get('{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]
                class_ = globals()[type_name_]
                obj_ = class_.factory()
                obj_.build(child_)
            else:
                raise NotImplementedError(
                    'Class not implemented for <Group> element')
            self.Group.append(obj_)
# end class GroupListType


class GroupType(GeneratedsSuper):
    """The GroupType type specifies a group that a user account belongs to.
    This is an abstract type since group IDs are operating-system
    specific, and is extended as needed in the derived CybOX object
    schemas."""
    subclass = None
    superclass = None
    def __init__(self):
        pass
    def factory(*args_, **kwargs_):
        if GroupType.subclass:
            return GroupType.subclass(*args_, **kwargs_)
        else:
            return GroupType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def export(self, outfile, level, namespace_='UserAccountObj:', name_='GroupType', namespacedef_=''):
        showIndent(outfile, level)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='GroupType')
        if self.hasContent_():
            outfile.write('>\n')
            self.exportChildren(outfile, level + 1, namespace_, name_)
            outfile.write('</%s%s>\n' % (namespace_, name_))
        else:
            outfile.write('/>\n')
    def exportAttributes(self, outfile, level, already_processed, namespace_='UserAccountObj:', name_='GroupType'):
        pass
    def exportChildren(self, outfile, level, namespace_='UserAccountObj:', name_='GroupType', fromsubclass_=False):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='GroupType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class GroupType


USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""

def usage():
    print USAGE_TEXT
    sys.exit(1)


def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = globals().get(tag)
    return tag, rootClass


def parse(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'User_Account'
        rootClass = UserAccountObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_=rootTag, 
        namespacedef_='')
    return rootObj


def parseString(inString):
    from StringIO import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'User_Account'
        rootClass = UserAccountObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_="User_Account",
        namespacedef_='')
    return rootObj


def parseLiteral(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'User_Account'
        rootClass = UserAccountObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('#from user_account_object import *\n\n')
    sys.stdout.write('import user_account_object as model_\n\n')
    sys.stdout.write('rootObj = model_.rootTag(\n')
    rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
    sys.stdout.write(')\n')
    return rootObj


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()


__all__ = [
    "GroupListType",
    "GroupType",
    "PrivilegeListType",
    "PrivilegeType",
    "UserAccountObjectType"
    ]
