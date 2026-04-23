--Bu kod "h1" kullanıcısını sistemde pasif bırakır.
UPDATE kullanıcılar SET durum='Pasif' WHERE id='h1';
--
--Bu kod sistemde "h1" kullanıcısını aktif hale getirir.
UPDATE kullanıcılar SET durum='Aktif' WHERE id='h1';
--
--Bu kod birden fazla kişiyi pasif hale getirir. [h1,h2,h3,h4,h5].
UPDATE kullanıcılar SET durum='Pasif' WHERE id IN ('h1', 'h2','h3','h4','h5')
--
--Bu kod sistemde birden fazla kişiyi aktif hale getirir. [h1,h2,h3,h4,h5].
UPDATE kullanıcılar SET durum='Aktif' WHERE id IN ('h1', 'h2','h3','h4','h5')


