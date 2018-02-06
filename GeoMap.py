import arcpy

str_dir_main = r"\\DEQHQ1\TMDL\TMDL_WR\MidCoast\GIS\Figures\Upper_Yaquina_Maps"
str_mxd_blank = r"Upper_Yaquina_TMDL_Blank_ME.mxd"
str_df_cur = r"Layers"
str_lyr_cur = r"UY_Geo.lyr"
str_mxd_save = r"Upper_Yaquina_TMDL_UY_Geo.mxd"

mxd = arcpy.mapping.MapDocument(str_dir_main + "\\" + str_mxd_blank)
df = arcpy.mapping.ListDataFrames(mxd, str_df_cur)[0]

addLayer2 = arcpy.mapping.Layer(str_dir_main + "\\" + str_lyr_cur)

arcpy.mapping.AddLayer(df, addLayer2, "BOTTOM")
arcpy.RefreshTOC()
arcpy.RefreshActiveView()

mxd.saveACopy(str_dir_main + "\\" + str_mxd_save)

del mxd, df, addLayer2
