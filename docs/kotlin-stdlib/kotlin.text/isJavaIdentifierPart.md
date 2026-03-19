

# isJavaIdentifierPart

Returns true if this  character (Unicode code point) may be part of a Java identifier as other than the first character.

```kotlin
inline fun Char.isJavaIdentifierPart(): Boolean(source)
```

```kotlin
fun main() {
    val text = "abc_123$def 456"
    val identifierChars = text.filter { it.isJavaIdentifierPart() }
    println(identifierChars)   // prints: abc_123def456
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/is-java-identifier-part.html)

    