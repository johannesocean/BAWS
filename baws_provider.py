# -*- coding: utf-8 -*-

"""
/***************************************************************************
 BAWS
                                 A QGIS plugin
 Manully adjust algae maps
                              -------------------
        begin                : 2019-04-17
        copyright            : (C) 2019 by SMHI
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
__author__ = 'SMHI'
__date__ = '2019-04-17'
__copyright__ = '(C) 2019 by SMHI'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

from qgis.core import QgsProcessingProvider, QgsProject
from processing.core.ProcessingConfig import Setting, ProcessingConfig
from .baws_algorithm import BAWSAlgorithm


class BAWSProvider(QgsProcessingProvider):
    """The plugin provider.

    According to template.
    """

    DUMMY_SETTING = 'DUMMY_SETTING'

    def __init__(self):
        """Initialize."""
        QgsProcessingProvider.__init__(self)

        # Deactivate provider by default
        self.activate = False

        # Load algorithms
        self.baws = BAWSAlgorithm()
        # self.alglist = [BAWSAlgorithm()]
        # for alg in self.alglist:
        #     alg.provider = self

    def id(self):
        """Return class name."""
        return self.__class__.__name__

    def name(self):
        """This is the name that will appear on the toolbox group.

        It is also used to create the command line name of all the
        algorithms from this provider.
        """
        return 'baws_provider'

    def initializeSettings(self):
        """In this method we add settings needed to configure our provider.

        Do not forget to call the parent method, since it takes care
        or automatically adding a setting for activating or
        deactivating the algorithms in the provider.
        """
        QgsProcessingProvider.initializeSettings(self)
        ProcessingConfig.addSetting(
            Setting(
                'Example algorithms',
                BAWSProvider.DUMMY_SETTING,
                'Example setting',
                'Default value'
            )
        )

    def unload(self):
        """Remove self.

        Setting should be removed here, so they do not appear anymore
        when the plugin is unloaded.
        """
        QgsProcessingProvider.unload(self)
        try:
            ProcessingConfig.removeSetting(BAWSProvider.DUMMY_SETTING)
        except:
            pass

    def getName(self):
        """This is the name that will appear on the toolbox group.

        It is also used to create the command line name of all the
        algorithms from this provider.
        """
        return self.name()

    def getDescription(self):
        """This is the provired full name."""
        return 'Provider of layers'

    def getIcon(self):
        """We return the default icon."""
        return QgsProcessingProvider.getIcon(self)

    def loadAlgorithms(self):
        """Here we fill the list of algorithms in self.algs.

        This method is called whenever the list of algorithms should
        be updated. If the list of algorithms can change (for instance,
        if it contains algorithms from user-defined scripts and a new
        script might have been added), you should create the list again
        here.

        In this case, since the list is always the same, we assign from
        the pre-made list. This assignment has to be done in this method
        even if the list does not change, since the self.algs list is
        cleared before calling this method.
        """
        self.algs = None
