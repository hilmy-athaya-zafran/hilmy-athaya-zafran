PGDMP      :                |           testing    16.3    16.3     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    32781    testing    DATABASE     �   CREATE DATABASE testing WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
    DROP DATABASE testing;
                postgres    false            �            1259    32782    tb1    TABLE     Y   CREATE TABLE public.tb1 (
    id integer NOT NULL,
    barang text,
    harga integer
);
    DROP TABLE public.tb1;
       public         heap    postgres    false            �          0    32782    tb1 
   TABLE DATA           0   COPY public.tb1 (id, barang, harga) FROM stdin;
    public          postgres    false    215   �                  2606    32786    tb1 tb1_pkey 
   CONSTRAINT     J   ALTER TABLE ONLY public.tb1
    ADD CONSTRAINT tb1_pkey PRIMARY KEY (id);
 6   ALTER TABLE ONLY public.tb1 DROP CONSTRAINT tb1_pkey;
       public            postgres    false    215            �   2   x�3�����I-**�42 .�@j�!�g�错���ihdA\1z\\\ �O�     