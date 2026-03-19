

# codePointBefore

Returns the character (Unicode code point) before the specified index.

```kotlin
inline fun String.codePointBefore(index: Int): Int(source)
```

```kotlin
val text = "Hello, world!"
val index = 12                     // position of the second 'l' in "world"
val codePoint = text.codePointBefore(index)

println("Code point before index $index: U+${codePoint.toString(16).uppercase()}")
println("Character: ${codePoint.toChar()}")
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/code-point-before.html)

    