

# toCharArray

Returns a CharArray containing characters of this string.

```kotlin
expect fun String.toCharArray(): CharArray(source)
```

```kotlin
fun main() {
    val text = "Hello, Kotlin!"
    val charArray = text.toCharArray()
    println(charArray.joinToString(", "))
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-char-array.html)

    