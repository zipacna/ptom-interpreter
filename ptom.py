class Ptom:
    """
    plaintext object markdown - a minimalistic textformat
    author: Jean Mattes
    author-uri: http://www.risingcode.net/
    """
    tabsep = '%5Ct'
    spacesep = '%20%20%20%20'
    newlinesep = '%5Cn'

    def __init__(self, file: str, op: str, txt='', raw=0):
        """
        :param file: to open
        :param op: operation to be executed
        """
        self.file = file
        self.handle = 0
        self.ptom = 0
        self.txt = txt
        self.raw = raw
        self.nodenew = ''
        if op == 'load':
            self.load()
        elif op == 'dump':
            self.dump()

    def __str__(self):
        """:return: Infos about current object"""
        return '\nfile:{},\nhandle:{},\nptom:{},\ntxt:{},\nraw:{}'.format(self.file, self.handle,
                                                                          self.ptom, self.txt,
                                                                          self.raw, self.nodenew)

    def load(self):
        """
        read the ptom file
        # TODO: handle \t (or 4 spaces) & \n
        """
        try:
            self.handle = open(self.file, 'r')
            self.ptom = self.handle.readlines()
            for node in self.ptom:
                for sep in ['\t', '    ', '\n']:
                    if sep in node:
                        depth = node
                        print('depth:', depth)
                        while isinstance(depth, list):
                            # TODO: scan full range, replace 0 with all possibilities
                            if depth.__len__() == 1:
                                depth = depth[0]
                            else:
                                raise OverflowError
                        nodeop = node.replace(sep, '')
                        self.nodenew = [nodeop]
                    else:
                        self.nodenew = '-'
                print(self.nodenew)
            if self.raw == 0:
                for line in self.ptom:
                    for sep in [self.tabsep, self.spacesep, self.newlinesep]:
                        for sepn in ['\t', '\t', '\n']:
                            line.replace(sep, sepn)
            if isinstance(self.ptom, list):
                print('\nLoading successful:', self.ptom)
            else:
                print('\nLoading failed')
        except (FileNotFoundError, TypeError, OverflowError) as error:
            print(error)
            print('Error while fetching ptom object/file: File not found or not readable')
            print('Error while traversing tree: Tree with no value/s, only key/s')
            print('Error while traversing tree: Index unresolvable')

    def dump(self):
        """
        dump into ptom file
        # TODO: handle \t (or 4 spaces) & \n
        """
        self.handle = open(self.file, 'w+')
        self.ptom = self.handle.writelines(self.txt)
        if self.ptom:
            print('\nWriting successful')
        else:
            print('\nWriting failed')
