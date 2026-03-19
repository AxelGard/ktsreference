

# concatToString

Concatenates characters in this CharArray into a String.

```kotlin
expect fun CharArray.concatToString(): String(source)
```

```kotlin
val chars = charArrayOf('H', 'e', 'l', 'l', 'o', ' ', 'K', 'o', 't', 'l', 'i', 'n')
val text = chars.concatToString()
println(text)   // Output: Hello Kotlin
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/concat-to-string.html)

    