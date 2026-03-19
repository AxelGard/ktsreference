

# mutableListOf

Returns an empty new MutableList.

```kotlin
inline fun <T> mutableListOf(): MutableList<T>(source)
```

```kotlin
val names = mutableListOf<String>()   // create an empty mutable list

// add elements
names += "Alice"
names += "Bob"
names.addAll(listOf("Charlie", "Diana"))

// iterate and print each element
for (name in names) {
    println(name)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/mutable-list-of.html)

    