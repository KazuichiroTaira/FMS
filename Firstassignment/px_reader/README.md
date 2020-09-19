From https://github.com/ljleppan/py3-opendata

To read files into Pandas DataFrames

    import px_reader
    px_obj = px_reader.Px('a_px_file_on_filesystem.px')
    pandas_dataframe = px_obj.pd_dataframe()