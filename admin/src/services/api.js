import axios from './request.js';

const api = {
  /* auth */
  login: data => axios.post('auth/login', data),

  register: data => axios.post('auth/register', data),

  /* category */
  getCategoryList: data => axios.get('category/list', { params: { all: data.showAll } }),

  createCategory: data => axios.post('category/create', data),

  deleteCategory: data => axios.get(`category/delete/${data.id}`),

  updateCategory: data => axios.post(`category/update/${data.id}`, data),

  /* tag */
  getTagList: data => axios.get('tag/list', { params: { all: data.showAll } }),

  createTag: data => axios.post('tag/create', data),

  deleteTag: data => axios.get(`tag/delete/${data.id}`),

  updateTag: data => axios.post(`tag/update/${data.id}`, data),

  /* article */
  getArticleList: data => axios.get('article/list', { params: data }),
  
  getArticleDetail: data => axios.get(`article/${data.id}`),

  createArticle: data => axios.post('article/create', data),

  deleteArticle: data => axios.get(`article/delete/${data.id}`),

  updateArticle: data => axios.post(`article/update/${data.id}`, data),

  uploadImg: data => axios.post(`upload`, data, { headers: {'Content-Type': 'multipart/form-data'}}),
}

export default api