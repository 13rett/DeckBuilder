"""
This program will use the CardController.json and any provided and defined images to create a custom deck of cards.
    Written By 13rett Graves in 2021 using Python 3.9.6 & Pillow 8.3.1

Program Parameters:
    -h, --help
        Valid inputs:
            None. This just triggers this doc string to be printed in console.
    -x, --width, -card_width
        Valid inputs:
            Any positive integer. This determines the final card's width in pixels.
    -h, --height, -card_height
        Valid inputs:
            Any positive integer. This determines the final card's height in pixels.
    -c, --controller, --json
        Valid inputs:
            any path string to the controller.json you wish to use. Starting at the directory that the program is being run from.
            ex. "/Example/Elements.json" would run the Elements.json in the /Example/ folder
    -d, -n, --deck, --name, --deckname
        Valid inputs:
            any string
    -o, --output, --out
        Valid inputs:
            any path string starting at the directory that the program is being run from.
    -r, --scale, --res, --resolution, --card_scale
        Valid inputs:
            The scale-factor to increase the cards by.
    !!Not Implemented Yet!! -s, --sheet, --stitch
        Valid inputs:
            i = exports the cards as individual cards
            a = exports the cards as a square sheet based on the number of cards
            <#>x<#> = makes sheets of the predefined number of cards until all cards are included. the first <#> is the columns, the x is static as a seperator and the second <#> is the number of rows.


FileStructure:
    /~
        /Imgs
            /Suits
                /{SuitID}.png
                    This is the icons for each Suit (The club, diamond, sword, etc) & used for any "Suit" icons for it's suit.
            /Unique
                /{IconID}.png
                    This is the various images for face cards, unique cards, non-suit cards, or various miscellaneous images on some/many/all cards such as a watermark or background image.
        DeckMaker.py
            This is the program file.
        CardController.json
            DeckControl: This is a set of CardController options that can determine various properties of the deck such as the save location, the size of the cards, and if the cards are saved as a sheet.
                Options:
                    DeckName: The name of the Deck. Used to determine the name of the folder cards are saved within.
                    Width: A numerical value to control the width of the card. When multiplied by Scaler this determines the number of pixels the cards width is.
                    Height: A numerical value to control the height of the card. When multiplied by Scaler this determines the number of pixels the cards height is.
                    Scaler: An Int that multiplies the Width and Height to control card size without affecting the size ratio.
                    Savefolder: This file-path string determines where the deck's save folder is located. This file-path begins within the running directory.
                    !!Not Implemented Yet!! Sheet: If set to "True" the program will export a sheet of the cards in a sub-folder called sheets.
                    !!Not Implemented Yet!! SheetX: This is only used when Sheet is "True" and SheetY is also included. When set to an integer it will ensure the card sheet is this many cards wide.
                    !!Not Implemented Yet!! SheetY: This is only used when Sheet is "True" and SheetX is also included. When set to an integer it will ensure the card sheet is this many cards high.
                    !!Not Implemented Yet!! SheetPad: This is only used when Sheet is "True". When set to an integer it will place that number of transparent pixels between each card and the edge or other cards. This can be overridden by SheetXPad & SheetYPad.
                    !!Not Implemented Yet!! SheetXPad: This is only used when Sheet is "True" and SheetYPad is also included. When set to an integer it will place that number of transparent pixels between each card and the edge in only the horizontal direction.
                    !!Not Implemented Yet!! SheetYPad: This is only used when Sheet is "True" and SheetXPad is also included. When set to an integer it will place that number of transparent pixels between each card and the edge in only the horizontal direction.
            Suits: This is the list of Suits that exist.
                Options:
                    SuitID: The name of the suit. Used to determine the first part of a card's save name. This should be unique to each suit.
                    Skip: If "True" this Suit will be skipped when making suit Cards. This can be used to save extra colors that will remain constant across many icons and change the color in all icons together.
                    SuitColor1: This is a hexcode color that is saved to the suit and can be accessed by the card icons to ensure a consistent color across many icons.
                    SuitColor2: This is a hexcode color that is saved to the suit and can be accessed by the card icons to ensure a consistent color across many icons.
                    SuitColor3: This is a hexcode color that is saved to the suit and can be accessed by the card icons to ensure a consistent color across many icons.
                    SuitColor4: This is a hexcode color that is saved to the suit and can be accessed by the card icons to ensure a consistent color across many icons.
                    SuitCopies: This integer determines how many times the cards for a suit are saved. This is multiplicative with the CopyNumber that a card can have.
                    IconImg: This file-path string determines where the suit's icon image is loaded from. This file-path begins within the running directory. If not set then any suit icons will attempt to use an image in the '/Imgs/Suits/' folder that has the name of the SuitID and extension '.png' as it's icon. 
                    IconImg2: This file-path string acts the same as IconImg.
            SuitCards: This is the list of cards that will appear in each suit.
                Options:
                    CardID: The name of the card. Used to determine the second part of a card's save name. This should be unique to each card. 
                    Skip: If "True" this card will be skipped.
                    CopyNumber: This integer determines how many times a card in a suit is saved. This is multiplicative with the SuitCopies that a suit can have.
                    CardSuitOverride: This string should match the SuitID of one of the suits. The card will then act as if it is that suit. This will be inherited by any icons that do not contain an IconSuitOverride value but be overridden by those that do.
                    IconList: This is the list of images to use to build the card and where they will be placed on the card.
                        Skip: If "True" this icon will be skipped.
                        Left: This number should define where the left side of the icon's bounding box is as a percentage of the card width.
                        Right: This number should define where the right side of the icon's bounding box is as a percentage of the card width.
                        Top: This number should define where the top of the icon's bounding box is as a percentage of the card height.
                        Bottom: This number should define where the bottom of the icon's bounding box is as a percentage of the card height.
                        ReverseCard: If "True" this icon will be applied as if the card is turned upside down.
                        ProportionLock: Determines if the icon should be stretched to fit or scaled so that it retains it's aspect ratio. It can be in the following values:
                            "S": Stretches to fit.
                            "H": Sizes it to match height.
                            "W": Sizes it to match width.
                            "F": Sizes it to match the smaller of height or width. This is the default if no ProportionLock is included.
                        Rotation: This number will rotate the image counterclockwise a number of degrees equal to it's value.
                        IconSuitOverride: This string should match the SuitID of one of the suits. The icon will then act as if it is that suit for the purposes of ColorOverride.
                        !!Not Implemented Yet!! "PreText": This will be prepended to the start of text icons.
                        !!Not Implemented Yet!! "PostText": This will be prepended to the end of text icons.
                        Type: This determines what kind of icon is added. It can be in the following values:
                            "Suit" will place the IconImg of the icon's suit.
                            "ID" will add the first character of the CardID to the card.
                            "SuitID" will add the SuitID of the icon's suit onto the card.
                            "Txt" will add the text in the icon's Value to the card. The Value should be a string of the text you want added to the card. The icon must also contain a Value when Type is "Txt".
                            "Unique" will place the image defined by the icon's Value. The Value should be a file-path string to the image you want to use. This file-path begins within the running directory. The icon must also contain a Value when Type is "Unique".
                        Value: This provides additional data used by some Type values.
                        ColorOverride: This string will recolor the icon image so that the black values are the given color. White colors remain white and any mid-tones will be converted to the proportional mid-tone between white and the provided color. This does not change any transparency values. It can be in the following values:
                            A hexcode string in the "#RRGGBB" format will use that hexcode color.
                            "Suit1" will use SuitColor1 of the icon's suit.
                            "Suit2" will use SuitColor2 of the icon's suit.
                            "Suit3" will use SuitColor3 of the icon's suit.
                            "Suit4" will use SuitColor4 of the icon's suit.
            UniqueCards: This is the list of cards that do not belong to a suit or that must be uniquely constructed for the suits preventing them from being included in the SuitCards list.
                Options match the SuitCards options except as follows:
                    If a CardSuitOverride is provided then the CardID can match so long as the CardSuitOverride does not match.
                    Icons:
                        Either CardSuitOverride or IconSuitOverride must be provided if Type is "Suit" or "SuitID".
                        Either CardSuitOverride or IconSuitOverride must be provided if ColorOverride is "Suit1", "Suit2", "Suit3", or "Suit4".

"""

import sys, os, getopt, json
from PIL import Image, ImageDraw, ImageFont, ImageOps

def main(argv):
    RUNNING_DIR = os.path.dirname(__file__)

    # This is what json file will be used to generate all the cards
    CARD_CONTROLLER = 'CardController.json'


    CARD_WIDTH = 0
    CARD_HEIGHT = 0
    CARD_RATIO = 0
    CARD_SCALE = 0
    DECK_NAME = ''
    CARDLIST = []
    SHEET = None
    SHEET_DIMENSIONS = None
    SHEET_PADDING = None
    SAVE_LOC = None

    # This sets any arguments given from the startup command
    try:
        opts, args = getopt.getopt(argv,"hx:y:c:d:n:o:s:r:",["help=","width=","card_width=","height=","card_height=","controller=","json=","deck=","name=","deckname=","sheet=","stitch=","output=","out=","scale=","res=","resolution=","card_scale=","sheet_padding=","sheet_pad="])
    except getopt.GetoptError:
        print(argv)
        print('Error: Deckmaker.py')
        print(__doc__)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(__doc__)
            sys.exit()
        elif opt in ("-x","--width","--CARD_WIDTH"):
            CARD_WIDTH = int(arg)
        elif opt in ("-y","--height","--CARD_HEIGHT"):
            CARD_HEIGHT = int(arg)
        elif opt in ("-c","--controller","--json"):
            CARD_CONTROLLER = arg
        elif opt in ("-d","--deck","--n","--name","--deckname"):
            DECK_NAME = arg
        elif opt in ("-s","--sheet","--stitch"):
            if arg == "i":
                SHEET = False
            elif arg == "a":
                SHEET = True
            elif arg == "#X#":
                SHEET = True
                # TODO: Replace 3x3 hardcode with the values of the input
                SHEET_DIMENSIONS = [3,3]
        elif opt in ("--sheet_padding","--"):
            SHEET_PADDING = (int(arg), int(arg))
        elif opt in ("-o","--output","--out","--sheet_pad"):
            SAVE_LOC = arg
        elif opt in ("-r","--scale","--res","--resolution","--card_scale"):
            CARD_SCALE = arg

    # Read the SuitsController.json file into a dict called CONTROLLER_DATA
    CONTROLLER_DATA = None
    try:
        with open(RUNNING_DIR + '/' + CARD_CONTROLLER) as f:
            CONTROLLER_DATA = json.load(f)
    except Exception as e:
        print('Error opening file. ' + RUNNING_DIR + '/' + CARD_CONTROLLER + '\n\t' + str(e))
        sys.exit(2)


    # If the values are not set by command line it attempts to set them via the CardController.json, failure setting them to hardcoded defaults.
    if CARD_SCALE <= 0:
        try:
            CARD_SCALE = int(CONTROLLER_DATA['DeckControl']['Scaler'])
        except:
            CARD_SCALE = 1
    if CARD_WIDTH == 0:
        try:
            CARD_WIDTH = int(CONTROLLER_DATA['DeckControl']['Width'] * CARD_SCALE)
        except:
            CARD_WIDTH = int(675 * CARD_SCALE)
    if CARD_HEIGHT == 0:
        try:
            CARD_HEIGHT = int(CONTROLLER_DATA['DeckControl']['Height'] * CARD_SCALE)
        except:
            CARD_HEIGHT = int(1050 * CARD_SCALE)
    CARD_RATIO = CARD_WIDTH / CARD_HEIGHT
    if SAVE_LOC == None:
        try:
            SAVE_LOC = CONTROLLER_DATA['DeckControl']['Savefolder']
        except:
            None
    if DECK_NAME == '':
        try:
            DECK_NAME = CONTROLLER_DATA['DeckControl']['DeckName']
        except:
            DECK_NAME = 'Deck'
    if SHEET == None:
        try:
            SHEET = CONTROLLER_DATA['DeckControl']['Sheet']
        except:
            SHEET = False
    if SHEET == True and SHEET_DIMENSIONS == None:
        try:
            SHEET_DIMENSIONS = (int(CONTROLLER_DATA['DeckControl']['SheetX']), int(CONTROLLER_DATA['DeckControl']['SheetY']))
        except:
            None
    if SHEET == True and SHEET_PADDING == None:
        try:
            SHEET_PADDING = (int(CONTROLLER_DATA['DeckControl']['SheetXPad']), int(CONTROLLER_DATA['DeckControl']['SheetYPad']))
        except:
            None
    if SHEET == True and SHEET_PADDING == None:
        try:
            SHEET_PADDING = (int(CONTROLLER_DATA['DeckControl']['SheetPad']), int(CONTROLLER_DATA['DeckControl']['SheetPad']))
        except:
            None

    print('Running:' + os.path.basename(__file__) + ' in ' + RUNNING_DIR + ' using ' + CARD_CONTROLLER)
    print('Cardsize:' + str(CARD_WIDTH) + 'x' + str(CARD_HEIGHT) + ' for Deck:' + DECK_NAME + ' Cardsheet:' + (str(SHEET_DIMENSIONS) if SHEET_DIMENSIONS != None else str(SHEET)))
    print()

    class Suit:
        """ This class holds the details for a Suit so that they can be referenced quickly and repeatedly without needing to navigate the CARD_CONTROLLER dict 
        Contains:
            id
                A string that acts as the name for the suit. It is used in saving and finding the Suit image if icon is not defined.
            color1
                This is the primary color, generally saved as a hex code in '#RRGGBB' format
            color2
                This is a secondary color for accents or contrasts and formatted the same as color1
            suitCopies
                This is how many times the suit will be saved. This is multiplicative with the count that a card appears within a suit.
                (ex. If the 'Blue' Suit has 2 copies and the 'Skip' card appears 3 times for each suit then there will be 6 'Blue Skip' cards)
            icon
                This is the filepath to use for the icon image starting at the RUNNING_DIR. this defaults to '/Imgs/Suits/' + self.id + '.png'
        """
        def __init__(self, id, color1 = '#000000', color2 = '#666666', color3 = '#999999', color4 = '#FFFFFF', suitCopies = 1, icon = '', icon2 = ''):
            self.id = str(id)
            self.skip = False
            self.color1 = color1
            self.color2 = color2
            self.color3 = color3
            self.color4 = color4
            self.suitCopies = suitCopies
            if icon == '':
                self.icon = '/Imgs/Suits/' + str(self.id) + '.png'
            else:
                self.icon = icon
            if icon2 == '':
                self.icon2 = '/Imgs/Suits/' + str(self.id) + '_2.png'
            else:
                self.icon2 = icon2

    # This function takes in the dict entry for a card 
    def makeCardImg(cardData, passedSuit = None, saveLoc = ''):
        """ This function takes the cardData that was passed and creates then saves an image from it 
        params:
            cardData
                This takes in the dict object of the card as it was imported from the json file.
            passedSuit
                This is the default suit used for any icons, suitColors and the cardName
                If None then any cards/icons that use a suit specific detail without an override will print an error and be skipped on image creation
            saveLoc
                This is the location that the results are saved.
                If not given it will save to the RUNNING_DIR+'/'+DECK_NAME folder. This may result in extra cards if different decks are created with additional suits or names and will overwrite existing cards of the same suit and name.
        """
        # if "Skip is true then it skips making the card
        try:
            if (cardData['Skip'] == "True"):
                # print('\tSkipping Card:\n\t\t' + str(cardData))
                return
        except:
            None

        c = Image.new('RGBA', (CARD_WIDTH,CARD_HEIGHT), (0,0,0,0))
        icons = cardData['IconList']
        copyNumber = 1
        s = passedSuit

        # Just save to Running Folder if no saveLoc is provided
        if (saveLoc == ''):
            saveLoc = RUNNING_DIR + '/' + DECK_NAME + '_Cards'
            if (os.path.exists(saveLoc) == False):
                os.makedirs(saveLoc)

        # This can override the Suit of a card. if CardSuitOverride exists for a card (This looks at the Card level for CardSuitOverride not the Icon level.)
        try:
            overrideID = str(cardData['CardSuitOverride'])
            # if the override does not exist then it will escape out before this loop due to the dict not having the CardSuitOverride
            for override in suitList:
                if override.id == overrideID:
                    s = override
        except:
            None

        # This goes over each icon in the card's list of icons and adds it to the card. If an icon errors it will print the error and move to the next icon
        for i in range(len(icons)):
            # if "Skip is true it skips to the next icon
            try:
                if (icons[i]['Skip'] == "True"):
                    continue
            except:
                None
            try:
                # The variables needed per icon.
                iconImg = None
                Lef = 0
                Rig = 100
                Top = 0
                Bot = 100
                iconSuit = s
                spin = 0
                color = None
                propLock = None
                scaleX = 1
                scaleY = 1
                reversed = False


                # This is where the icon's size and position are set.
                try:
                    Lef = icons[i]['Left']
                except:
                    None
                try:
                    Rig = icons[i]['Right']
                except:
                    None
                try:
                    Top = icons[i]['Top']
                except:
                    None
                try:
                    Bot = icons[i]['Bottom']
                except:
                    None

                # This is where an icon can use the properties of another Suit
                try:
                    overrideID = str(icons[i]['IconSuitOverride'])
                    # if the override does not exist then it will escape out before this loop due to the dict not having the IconSuitOverride
                    for override in suitList:
                        if override.id == overrideID:
                            iconSuit = override
                except:
                    None

                # This is where the icon's rotation property is set if it exists
                try:
                    spin = int(icons[i]['Rotation'])
                except:
                    None

                # This is where the icon's proportion lock is set if it exists
                try:
                    propLock = str(icons[i]['ProportionLock'])
                except:
                    propLock = 'F'

                # This is where the icon's ColorOverride property is set if it exists
                try:
                    color = str(icons[i]['ColorOverride'])
                except:
                    None
                if color == 'Suit1':
                    color = iconSuit.color1
                elif color == 'Suit2':
                    color = iconSuit.color2
                elif color == 'Suit3':
                    color = iconSuit.color3
                elif color == 'Suit4':
                    color = iconSuit.color4

                # This determines if the icon should be applied to the card as if rotated 180 degrees.
                try:
                    reversed = bool(icons[i]['ReverseCard'])
                except:
                    None

                # Here it determines what type of icon to add: suit, A letter, a Face, other images
                if(icons[i]['Type'] == 'Suit'):
                    iconImg = Image.open(RUNNING_DIR + str(iconSuit.icon))
                elif(icons[i]['Type'] == 'Suit2'):
                    iconImg = Image.open(RUNNING_DIR + str(iconSuit.icon2))
                elif (icons[i]['Type'] == 'Txt'):
                    value = icons[i]['Value'];
                    usedFont = ImageFont.load_default()
                    try:
                        usedFont = ImageFont.truetype('arial.ttf', size = 500)
                    except:
                        None
                    size = (usedFont.getsize(value)[0], usedFont.getsize(u"\u2588" + u"\u2573" + u"\u2593" )[1])
                    iconImg = Image.new('RGBA', (size[0], int(size[1])), (0,0,0,0))
                    draw = ImageDraw.Draw(iconImg)
                    draw.text((0,0),value,'#000000',usedFont)
                elif (icons[i]['Type'] == 'ID'):
                    value = str(cardData['CardID'])[0]
                    usedFont = ImageFont.load_default()
                    try:
                        usedFont = ImageFont.truetype('arial.ttf', size = 500)
                    except:
                        None
                    size = (usedFont.getsize(value)[0], usedFont.getsize(u"\u2588" + u"\u2573" + u"\u2593" )[1])
                    iconImg = Image.new('RGBA', (size[0], int(size[1])), (0,0,0,0))
                    draw = ImageDraw.Draw(iconImg)
                    draw.text((0,0),value,'#000000',usedFont)
                elif (icons[i]['Type'] == 'SuitID'):
                    idText = str(iconSuit.id)
                    usedFont = ImageFont.load_default()
                    try:
                        usedFont = ImageFont.truetype('arial.ttf', size = 500)
                    except:
                        None
                    size = (usedFont.getsize(idText)[0], usedFont.getsize(u"\u2588" + u"\u2573" + u"\u2593" )[1])
                    iconImg = Image.new('RGBA', (size[0], int(size[1])), (0,0,0,0))
                    draw = ImageDraw.Draw(iconImg)
                    draw.text((0,0),idText,'#000000',usedFont)
                elif (icons[i]['Type'] == 'Unique'):
                    iconImg = Image.open(RUNNING_DIR + icons[i]['Value'])
                else:
                    raise ValueError('Unknown Icon Type: ' + str(icons[i]['Type']))

                # This is where the icon's scale is set
                iconRatio = iconImg.size[0]/iconImg.size[1]
                if propLock in ['S','s','Stretch','stretch']:
                    #Stretch
                    scaleX = int((Rig - Lef)/100 * CARD_WIDTH )
                    scaleY = int((Bot - Top)/100 * CARD_HEIGHT )
                elif propLock in ['W','w','Width','width']:
                    #Width
                    scaleX = int((Rig - Lef)/100 * CARD_WIDTH )
                    scaleY = int(scaleX/iconRatio)
                elif propLock in ['H','h','Height','height']:
                    #Height
                    scaleY = int((Bot - Top)/100 * CARD_HEIGHT )
                    scaleX = int(scaleY*iconRatio)
                elif propLock in ['F','f','Fit','fit']:
                    #Fit
                    scaleX = int((Rig - Lef)/100 * CARD_WIDTH )
                    scaleY = int((Bot - Top)/100 * CARD_HEIGHT )
                    if scaleY >= scaleX:
                        scaleX = int(scaleY*iconRatio)
                    else:
                        scaleY = int(scaleX/iconRatio)

                iconImg = iconImg.resize( (scaleX, scaleY) ).rotate(spin)
                if (color != None):
                    img2 = iconImg
                    img2 = ImageOps.colorize(ImageOps.grayscale(img2), color, '#FFFFFF')
                    img2.putalpha(iconImg.getchannel('A'))
                    iconImg = img2

                if reversed:
                    img2 = Image.new('RGBA', (CARD_WIDTH,CARD_HEIGHT), (0,0,0,0))
                    img2.alpha_composite(iconImg, (int(Lef/100 * CARD_WIDTH), int(Top/100 * CARD_HEIGHT)), (0,0))
                    iconImg = img2.rotate(180)
                    Lef = 0
                    Top = 0

                c.alpha_composite(iconImg, (int(Lef/100 * CARD_WIDTH), int(Top/100 * CARD_HEIGHT)), (0,0))
            except Exception as e:
                print('\tError on Card:' + str(cardData) +'\n\t\tIcon:' + str(icons[i]) + '\n\t\tError: ' + str(e))
        # This is what determines how many card copies there are based on the card's CopyNumber and the suits SuitCopies
        try:
            copyNumber *= int(cardData['CopyNumber'])
        except:
            None
        try:
            copyNumber *= int(s.suitCopies)
        except:
            None
        for i in range(copyNumber):
            saveName = ('Unique' if s == None else str(s.id)) + '-' + str(cardData['CardID']) + (('-#' + str(i+1)) if copyNumber > 1 else '') + '.png'
            c.save(saveLoc + '/' +saveName)
            CARDLIST.append(saveName)
        return

    # convert the Suits list in the SuitsController.json into an array of the Suit class 
    suitList = []
    for i in range(len(CONTROLLER_DATA['Suits'])):
        s = Suit(id = CONTROLLER_DATA['Suits'][i]['SuitID'])
        try:
            s.color1 = CONTROLLER_DATA['Suits'][i]['SuitColor1']
        except:
            None
        try:
            s.color2 = CONTROLLER_DATA['Suits'][i]['SuitColor2']
        except:
            None
        try:
            s.color3 = CONTROLLER_DATA['Suits'][i]['SuitColor3']
        except:
            None
        try:
            s.color4 = CONTROLLER_DATA['Suits'][i]['SuitColor4']
        except:
            None
        try:
            s.suitCopies = CONTROLLER_DATA['Suits'][i]['SuitCopies']
        except:
            None
        try:
            s.icon = CONTROLLER_DATA['Suits'][i]['IconImg']
        except:
            None
        try:
            s.icon2 = CONTROLLER_DATA['Suits'][i]['IconImg2']
        except:
            None
        try:
            s.skip = CONTROLLER_DATA['Suits'][i]['Skip']
        except:
            None
        suitList.append( s )

    # Makes the save folder if it doesn't exist and creates a new folder if none are specified
    if(SAVE_LOC == None):
        # If no Save Location is given then it makes one in the Imgs folder based on deck name in a way that won't collide with previous runs
        SAVE_LOC = RUNNING_DIR + '/Results/' + DECK_NAME
        if (os.path.exists(SAVE_LOC)):
            DeckCounter = 0
            while (os.path.exists(SAVE_LOC + '_' + str(DeckCounter))):
                DeckCounter += 1
            SAVE_LOC = SAVE_LOC + '_' + str(DeckCounter)
    else:
        SAVE_LOC = RUNNING_DIR + '/' +  SAVE_LOC + DECK_NAME
    if (os.path.exists(SAVE_LOC+ '/cards') == False):
        os.makedirs(SAVE_LOC+ '/cards')
    if (SHEET and os.path.exists(SAVE_LOC+ '/sheets') == False):
        os.makedirs(SAVE_LOC+ '/sheets')


    print('Saving to: ' + str(SAVE_LOC))


    # Makes the cards for each Suit
    # Prints the current Suit when a new Suit starts.
    for i in suitList:
        if i.skip:
            continue
        # For each Suit Card it will run makeCardImg() for the current suit.
        print(i.id, ' x' + str(i.suitCopies), i.color1,i.color2)
        for j in range(len(CONTROLLER_DATA['SuitCards'])):
            makeCardImg(cardData = CONTROLLER_DATA['SuitCards'][j], passedSuit = i, saveLoc = SAVE_LOC+ '/cards')
        print()

    # Makes the Unique/non-Suit cards
    # Prints Unique to signify that the Unique cards have started being made.
    print('Unique Cards')
    for i in range(len(CONTROLLER_DATA['UniqueCards'])):
            makeCardImg(cardData = CONTROLLER_DATA['UniqueCards'][i], saveLoc = SAVE_LOC+ '/cards')
    print('\nFinished making cards.\n\n')

    listFile = open(SAVE_LOC+'/CardList.txt', 'w')
    for c in CARDLIST:
        listFile.write(c+'\n')


# Runs main
if __name__ == "__main__":
   main(sys.argv[1:])