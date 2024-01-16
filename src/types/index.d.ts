/*
 * @Author: GAO GAO
 * @Date: 2023-11-25 15:27:04
 */
type ArticleSection = {
  title?: string;
  content: string;
};

type ArticleFooter = {
  content: string;
};

type Article = {
  title: string;
  time: string;
  section: ArticleSection[];
  footer?: string | ArticleFooter[];
};
