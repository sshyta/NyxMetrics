PGDMP      6                }         	   NyxMetric    16.8    17.4     Z           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            [           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            \           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            ]           1262    16388 	   NyxMetric    DATABASE     w   CREATE DATABASE "NyxMetric" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'ru_RU.UTF-8';
    DROP DATABASE "NyxMetric";
                     postgres    false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
                     pg_database_owner    false            ^           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                        pg_database_owner    false    4            �            1259    16397    users    TABLE        CREATE TABLE public.users (
    id integer NOT NULL,
    login character varying(255),
    user_pass character varying(255)
);
    DROP TABLE public.users;
       public         heap r       postgres    false    4            �            1259    16396    users_id_seq    SEQUENCE     �   CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.users_id_seq;
       public               postgres    false    4    216            _           0    0    users_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;
          public               postgres    false    215            �           2604    16400    users id    DEFAULT     d   ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);
 7   ALTER TABLE public.users ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    216    215    216            W          0    16397    users 
   TABLE DATA                 public               postgres    false    216   �       `           0    0    users_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.users_id_seq', 6, true);
          public               postgres    false    215            �           2606    16404    users users_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public                 postgres    false    216            W   �   x����n�@ ��=O14!��+Z��E��E`Ӡ3�QA�O_ܹnw'g����M /@�r۝�^�5�5`D�N�V"x<_��i� 2��`��@�pI+a���'
�������6�_)�n��33I/�2�U�.��ǽ?ͿƆ�ʂiB����1���<ع�s;֒��f�}�"M�V�����&�lm�+���/5�������}cL,���❙�(���ҥ�hI*CكK�(t{Yb��3�Uj�ʃ�q��y.     