

# isISOControl

Returns true if this character is an ISO control character.

```kotlin
expect fun Char.isISOControl(): Boolean(source)
```

```kotlin
fun main() {
    val testChars = listOf('A', '\u0001', '\n', 'Z')
    for (c in testChars) {
        println("Character '${c}' is ISO control: ${c.isISOControl()}")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/is-i-s-o-control.html)

    