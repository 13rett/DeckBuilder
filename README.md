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
