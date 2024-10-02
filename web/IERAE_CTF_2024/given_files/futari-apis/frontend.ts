const FLAG: string = Deno.env.get("FLAG") || "IERAE{dummy}";
const USER_SEARCH_API: string = Deno.env.get("USER_SEARCH_API") ||
  "http://user-search:3000";
const PORT: number = parseInt(Deno.env.get("PORT") || "3000");

async function searchUser(user: string, userSearchAPI: string) {
  const uri = new URL(`${user}?apiKey=${FLAG}`, userSearchAPI);
  return await fetch(uri);
}

async function handler(req: Request): Promise<Response> {
  const url = new URL(req.url);
  switch (url.pathname) {
    case "/search": {
      const user = url.searchParams.get("user") || "";
      return await searchUser(user, USER_SEARCH_API);
    }
    default:
      return new Response("Not found.");
  }
}

Deno.serve({ port: PORT, handler });
