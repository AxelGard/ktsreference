

# isJavaIdentifierStart

Returns true if this character is permissible as the first character in a Java identifier.

```kotlin
inline fun Char.isJavaIdentifierStart(): Boolean(source)
```

```kotlin
fun main() {
    val c = '3'
    if (c.isJavaIdentifierStart()) {
        println("$c is a valid starting character for a Java identifier")
    } else {
        println("$c is NOT a valid starting character for a Java identifier")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/is-java-identifier-start.html)

    