

# category

Returns the Unicode general category of this character.

```kotlin
expect val Char.category: CharCategory(source)
```

```kotlin
fun main() {
    val chars = listOf('A', 'ß', 'π', '1', '♔')
    for (c in chars) {
        println("$c → ${c.category}")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/category.html)

    