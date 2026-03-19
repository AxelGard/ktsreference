

# replaceRange

Returns a char sequence with content of this char sequence where its part at the given range is replaced with the replacement char sequence.

```kotlin
fun CharSequence.replaceRange(startIndex: Int, endIndex: Int, replacement: CharSequence): CharSequence(source)
```

```kotlin
fun main() {
    val original = "Hello, World!"
    val modified = original.replaceRange(7, 12, "Kotlin")
    println(modified) // Hello, Kotlin!
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/replace-range.html)

    