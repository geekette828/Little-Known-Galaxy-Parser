Collection of Parser Items for the Little-Known Galaxy wiki found at: https://lkg.wiki.gg/ <br>
Putting these into output files, so we can do a compare between patches, and only update pages that need it.

# Parser Collections --
item_description_parser.py --<br>
  Creates a lua file that can be dropped directly into `https://lkg.wiki.gg/wiki/Module:Description/data` to update all of the descriptions of all of the items, and it will update the infobox.
  
dialogue_parser.py -- <br>
  Looks at a file folder: `Input/Assets/TextAsset` (should be replaced with each patch)<br>
  Parses the `English_NPCNAME.txt` files into a format used by the wiki. WIKI: Each region should be a section on the NPC's /Dialogue page. Emotes to text should be associated correctly.<br>
  Puts each file in file folder: Output/Dialogues<br>

email_parser.py -- <br>
  Looks at a email file in folder: `Input/Assets/TextAsset` (should be replaced with each patch)<br>
  Looks at asset files in `Input/Assets/MonoBehavior` to map email attachments.<br>
  Puts results in file folder: Output/Emails<br>

infobox_item_parser.py & infobox_seed_parser.py --<br>
  Looks at assets in `Input/Assets/MonoBehavior`, and creates a mock infobox template of item data.<br>
  Super versions of the same item are included in the base-item template.<br>
  Three results are generated - one of just seeds, one of everything with sell price (minus seeds), and one where the items can't be sold. This should make it easier to check for changes to sell price. <br>

loot_list_parser.py & loot_table_parser.py -- <br>
  Creates a loot_table_list of assets in `Input/Assets/MonoBehavior` that have a `lootTable`.<br>
  loot_list creates an output of loot droped from various things, like digging or meteorites. These lists hold both items and loot tables.<br>
  loot_table creates an output of loot tables, to be put in the `Data:Loot Tables` page, these do not have nested loot tables within them.<br>
  Each output is formated as it would be needed on the wiki.<br>

mission_infobox.py --<br>
  Creates a list of mission infoboxes, in proper wiki format.<br>

missions_npc_bb_item_request.py --<br>
  Creates a list of items different NPCs will request from bulletin board missions.<br>

npc_gift_overrides_parser.py --<br>
  Creates a list of npcs, then looks at their .assets for gives they love/like/are neutral twoards/dislike.<br>
  Puts results in file folder: Output/Gifts<br>

npc_gifts_to_player_parser.py --<br>
  Creates a list of items the npcs give to the player, both from friendship emails and dialogues after starting missions.<br>
  Puts results in the file folder: Output/Gifts<br>

recipe_crafting_parser.py --<br>
  Looks at assets files in `Input/Assets/MonoBehavior` that start with `crafting_` to get a product, quantity, ingredients, quantity<br>
  Looks at the product to get category and assigns a machine based on that category.<br>
  Puts results in file folder: Output/Recipes<br>

recipe_machine_production_parser.py --<br>
  First generates a file of all assets in `Input/Assets/MonoBehavior` with a "machine production" section in their asset file.<br>
  Then uses that list to iterate through the .assets of that list and pulls out recipie information. <br>
  Sorts the results by product, in the correct recipies template. <br>
  Puts results in the file folder: Output/Recipes<br>

shop_catalog_parser.py --<br>
  Looks at assets in `Input/Assets/MonoBehavior`, and creates a list of assets that start with `_StoreCatalog`.<br>
  It pulls out the `storeSets` information, then looks up all of the `storeItemsInSet` in each storeSet, then looks up the `itemForSale` to get the name of the item and buy price.<br>
  Formats everything in the shop template.<br>
  Outputs each shop into a different file in `Output/Shops`<br>

cutscenes_overview.py --<br>
  Dump of a bunch of cutscene information.

cutscenes_build_tree.py --<br>
  Builds a tree of cutscenes to follow in an order.

cutscenes_courting.py --<br>
  Creates a file for each of the RNPCs, with their date cinematic dialogue.

cutscenes_noncourting.py --<br>
  Creates a file that displays all other non-courting cutscenes. This output should be put in `Module:Cine/data`.

captain_rank_numbers.py --<br>
  Data dump of different ways to earn exp for the captain rank.

friendship_points.py --<br>
  Data dump of how to earn frienship points and their amounts for different actions.

library_sim.py --<br>
  Data dump of all of the books for the LIBRARY.sim. This output should be put in `Module:Library/data`.

# Util Scripts --<br>
guid_utils.py - All of the mapping stuff in one place.<br>
unity_yaml_loader.py - Custom constructor to handle Unity's specific YAML tags, in its own file for modularization, so it can be called from other scripts.

# Getting the Assets --
1. Download an application that allows you to look at the assets. I use [AssetRipper](https://github.com/AssetRipper/AssetRipper) for parsing and [AssetStudio](https://github.com/Perfare/AssetStudio) for sprites, and looking things up on the fly. For this parser I'll be using the file types that are extracted from AssetRipper. The scripts may need to be altarted if you use a different format.
2. In the preferred asset manager, load the `Little-Known Galaxy_Data` folder.
  * Windows: `C:/Program Files (x86)/Steam/steamapps/common/Little-Known Galaxy/Little-Known Galaxy_Data`
  * Linux: `${HOME}/.steam/steam/steamapps/common/Little-Known Galaxy/Little-Known Galaxy_Data`
3. Export -> All Files/Assets (depending on your preferred application). Put it into a folder, I prefer to put it in a folder with the patch number, but you do  you.

## Directory Structure
```
├── AuxiliaryFiles
└── ExportedProject
    ├── Assets
    │   ├── AnimationClip
    │   ├── AnimatorController
    │   ├── AnimatorOverrideController
    │   ├── AudioClip
    │   ├── AudioMixerController
    │   ├── Editor
    │   ├── Font
    │   ├── LightingSettings
    │   ├── Material
    │   ├── Mesh
    │   ├── MonoBehaviour     # This is where the character and item data is.
    │   ├── PhysicsMaterial2D
    │   ├── Plugins
    │   ├── PrefabInstance
    │   ├── RenderTexture
    │   ├── Resources
    │   ├── Scenes            # This is where the cutscene information is.
    │   ├── Scripts           # This holds various scripts that coorelates data.      
    │   ├── Shader
    │   ├── Sprite
    │   ├── StreamingAssets
    │   ├── TextAsset         # This is where the files for the email and dialogue parser are
    │   └── Texture2D
    ├── Packages
    └── ProjectSettings
```