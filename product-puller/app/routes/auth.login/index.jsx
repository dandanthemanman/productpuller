import { redirect } from "@remix-run/node";

// This route will be accessed when the store owner attempts to install your app
export let loader = async ({ request }) => {
  const shop = new URL(request.url).searchParams.get("shop");
  const redirectUri = `${process.env.SHOPIFY_APP_URL}/auth/callback`;
  const installUrl = `https://${shop}/admin/oauth/authorize?client_id=${process.env.SHOPIFY_API_KEY}&scope=read_products,write_orders&redirect_uri=${redirectUri}`;

  return redirect(installUrl);
};
