import os

from .element import Element

class HDAElement(Element):
    """
    Class describing houdini otls using the hda module
    """
    # export HOUDINI_PATH=$HOUDINI_PATH:'/users/grads/j/jmoborn/dusk/production;&'
    # if there is a directory called otls in this path, houdini will load any asset definitions from it
    # http://www.houdinitoolbox.com/installation.php

    @staticmethod
    def create_new_dict(name, department, parent_name):
        data_dict = Element.create_new_dict(name, department, parent_name)
        data_dict[Element.APP_EXT] = ".hdanc"
        return data_dict

    def publish(self, username, src, comment, status=None):
        """
        calls parent publish method. If a symbolic link to this element does not exist in the assembly dir, one is created.
        """
        Element.publish(self, username, src, comment, status)
        assembly_path = os.path.join(self._env.get_assembly_dir(), self.get_app_filename())
        if not os.path.exists(assembly_path):
            # create sym link
            os.symlink(self.get_app_filepath(), assembly_path)
            print self.get_app_filepath() + " -> " + assembly_path

    # def get_checkout_dir(self, username):
    #     """
    #     return the directory this element would be copied to during checkout for the given username.
    #     THE FOLLOWING IS TOTALLY FALSE
    #     This is overriden for otls because all checked out otls should be in the same directory,
    #     which needs to be called otls
    #     """
    #     return os.path.join(self._env.get_users_dir(), username, 'otls')
        