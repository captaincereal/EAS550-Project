def validate_non_null(df, column):
    return df[column].notna().all()


def validate_unique(df, columns):
    return not df.duplicated(columns).any()