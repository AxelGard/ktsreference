

# Char

Creates a Char with the specified code, or throws an exception if the code is out of Char.MIN_VALUE.code..Char.MAX_VALUE.code.

```kotlin
inline fun Char(code: Int): Char(source)
```

```kotlin
fun main() {
    val letterA = Char(65)          // 'A'
    val smile = Char(0x1F600)       // 😀
    val heart = Char(0x2665)        // ♥
    
    println("letterA: $letterA")
    println("smile: $smile")
    println("heart: $heart")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char.html)

    